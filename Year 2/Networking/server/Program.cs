using System;
using System.Data;
using System.Data.SqlTypes;
using System.Net;
using System.Net.NetworkInformation;
using System.Net.Sockets;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;

using LibData;

// ReceiveFrom();
class Program
{
    static void Main(string[] args)
    {
        ServerUDP.start();
    }
}

public class Setting
{
    public int ServerPortNumber { get; set; }
    public string? ServerIPAddress { get; set; }
    public int ClientPortNumber { get; set; }
    public string? ClientIPAddress { get; set; }
}


class ServerUDP
{
    static string configFile = Path.Combine(Directory.GetCurrentDirectory(), "Setting.json");    static string configContent = File.ReadAllText(configFile);
    internal static Setting? setting = JsonSerializer.Deserialize<Setting>(configContent);

    // TODO: [Read the JSON file and return the list of DNSRecords]
    static string dnsRecordsFile = @"DNSrecords.json";
    static string dnsRecordsContent = File.ReadAllText(dnsRecordsFile);
    internal static List<DNSRecord>? dnsRecordsList = JsonSerializer.Deserialize<List<DNSRecord>>(dnsRecordsContent);

    // TODO: [Create a socket and endpoints and bind it to the server IP address and port number]
    // This creates the server socket, reads IP and Port. Binds the socket to the endPoint
    static Socket serverSocket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
    static IPEndPoint localEndPoint = new IPEndPoint(IPAddress.Parse(setting.ServerIPAddress), setting.ServerPortNumber);

    // Buffer for incoming data
    static byte[] buffer = new byte[1024];
    static EndPoint remoteEndPoint = new IPEndPoint(IPAddress.Any, 0);

    static Random random = new Random();
    public static void start()
    {
        serverSocket.Bind(localEndPoint);

        Console.WriteLine($"Server started ({setting.ServerIPAddress}:{setting.ServerPortNumber}) Waiting for clients...");
        Message previousMessage = null;
        while (true)
        {
            try
            {
                Message message = ReceiveMessage();
                if (message == null) continue;

                // TODO:[Send Welcome to the client]
                if (message.MsgType == MessageType.Hello)
                {
                    SendMessage(WelcomeMessage());
                    previousMessage = message;
                }
                while (true)
                {
                    message = ReceiveMessage();

                    if (message.MsgType == MessageType.DNSLookup && (previousMessage.MsgType == MessageType.Hello | previousMessage.MsgType == MessageType.Ack))
                    {
                        // TODO:[Query the DNSRecord in Json file]
                        bool found = false;
                        foreach (DNSRecord dnsRecord in dnsRecordsList)
                        {
                            if (dnsRecord.Name == message.Content.ToString())
                            {

                                // TODO:[If found Send DNSLookupReply containing the DNSRecord]
                                SendMessage(DNSLookupReply(message.MsgId, dnsRecord));
                                found = true;
                                break;
                            }
                        }
                        // TODO:[If not found Send Error]
                        if (!found) { SendMessage(ErrorMessage()); continue; }
                        previousMessage = message;
                    }
                    else if (message.MsgType == MessageType.Ack && previousMessage.MsgType == MessageType.DNSLookup) previousMessage = message;
                    else if (message.MsgType == MessageType.End) break;
                    else
                    {
                        Console.WriteLine($"Error: Wrong Message order");
                    }
                }
                
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
    private static Message ErrorMessage()
    {
        Message errorMessage = new Message();
        errorMessage.MsgId = random.Next(999999);
        errorMessage.MsgType = MessageType.Error;
        errorMessage.Content = "Domain not found";
        return errorMessage;
    }
    private static Message DNSLookupReply(int messageID, DNSRecord dnsRecord)
    {
        Message DnSReply = new Message();
        DnSReply.MsgId = messageID;
        DnSReply.MsgType = MessageType.DNSLookupReply;
        DnSReply.Content = dnsRecord ;

        return DnSReply;
    }
    private static Message ReceiveMessage()
    {
        try
        {
            // This will block until a message is received
            int bytesReceived = serverSocket.ReceiveFrom(buffer, ref remoteEndPoint);

            string jsonMessage = Encoding.ASCII.GetString(buffer, 0, bytesReceived);

            Message? Message = JsonSerializer.Deserialize<Message>(jsonMessage);
            Console.WriteLine($"============================================================");
            Console.WriteLine($"Received from {remoteEndPoint} - MSG Type {Message.MsgType}: {Message.Content}");
            Console.WriteLine($"============================================================");
            return Message;
        }
        catch (SocketException ex) when (ex.SocketErrorCode == SocketError.TimedOut)
        {
            Console.WriteLine("No response received (timeout)");
            return null;
        }
    }
    private static void SendMessage(Message message)
    {
        string messageString = JsonSerializer.Serialize(message);
        byte[] responseData = Encoding.ASCII.GetBytes(messageString);
        serverSocket.SendTo(responseData, remoteEndPoint);
        Console.WriteLine($"============================================================");
        Console.WriteLine($"Message Send - MSG Type {message.MsgType}: {message.Content}");
        Console.WriteLine($"============================================================");
    }
    private static Message WelcomeMessage()
    {
        Message welcomeMessage = new Message();
        welcomeMessage.MsgId = 2;
        welcomeMessage.MsgType = MessageType.Welcome;
        welcomeMessage.Content = "Welcome Client";

        return welcomeMessage;
    }
}