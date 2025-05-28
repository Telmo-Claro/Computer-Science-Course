using System.Collections.Immutable;
using System.ComponentModel;
using System.Net;
using System.Net.Sockets;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using System.Text.Json.Nodes;
using System.Text.Json.Serialization;
using LibData;

class Program
{
    static void Main(string[] args)
    {
        ClientUDP.start();
    }
}

public class Setting
{
    public int ServerPortNumber { get; set; }
    public string? ServerIPAddress { get; set; }
    public int ClientPortNumber { get; set; }
    public string? ClientIPAddress { get; set; }
}

class ClientUDP
{
    static Random random = new Random();

    //TODO: [Deserialize Setting.json]
    static string configFile = Path.Combine(Directory.GetCurrentDirectory(), "Setting.json");
    static string configContent = File.ReadAllText(configFile);
    internal static Setting? setting = JsonSerializer.Deserialize<Setting>(configContent);

    //TODO: [Create endpoints and socket]
    static Socket clientSocket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);

    // Create Server Endpoint
    static IPEndPoint serverEndPoint = new IPEndPoint(IPAddress.Parse(setting.ServerIPAddress), setting.ServerPortNumber);

    static int messageInterval = 1000;

    static byte[] receiveBuffer = new byte[1024];
    static EndPoint remoteEndPoint = new IPEndPoint(IPAddress.Any, 0);


    public static void start()
    {
        

        Console.WriteLine($"UDP Client started. ({setting.ClientIPAddress}:{setting.ClientPortNumber})");
        {
            try
            {
                //TODO: [Create and send HELLO]
                Message helloMessage = HelloMessege();
                SendMessage(helloMessage);

                clientSocket.ReceiveTimeout = 5000;

                //TODO: [Receive and print Welcome from server]
                Message message = ReceiveMessage();
                if (message.MsgType != MessageType.Welcome)
                {
                    Console.WriteLine($"Wrong Message Order: Expected 'Welcome' got {message.MsgType}");
                    Environment.Exit(0);
                }

            }
            catch (Exception e)
            {
                Console.WriteLine($"Error: {e.Message}");
            }
        }
        // TODO: [Create and send DNSLookup Message]

        // Valid 1
        Message response = TestDnsLookup("www.outlook.com");

        // repeat the process until all DNSLoopkups (correct and incorrect onces) are sent to server and the replies with DNSLookupReply
        // valid 2
        response = TestDnsLookup("www.test.com");

        // invalid 1
        response = TestDnsLookup("asdasdasd");

        // invalid 3
        response = TestDnsLookup("324234234");

        //TODO: [Receive and print End from server]
        SendMessage(EndMessage());

    }
    private static Message TestDnsLookup(string url)
    {
        Message response = DnsLookup(url);
        if (response != null && response.MsgType == MessageType.DNSLookupReply)
        {
            //TODO: [Send Acknowledgment to Server]
            SendMessage(Ack(response.MsgId));
        }
        else if (response.MsgType != MessageType.Error)
        {
            Console.WriteLine($"Wrong Message Order: Expected 'DNSLookupReply' got {(response == null ? "null" : response.MsgType )}");
        }
        return response;
    }

    private static Message EndMessage()
    {
        Message endMessage = new Message();
        endMessage.MsgId = random.Next(999999);
        endMessage.MsgType = MessageType.End;
        endMessage.Content = "No Lookups anymore";

        return endMessage;
    }
    private static Message Ack(int msgID)
    {
        Message helloMessage = new Message();
        helloMessage.MsgId = random.Next(999999);
        helloMessage.MsgType = MessageType.Ack;
        helloMessage.Content = msgID;

        return helloMessage;
    }
    private static Message DnsLookup(string Domain)
    {
        try
        {
            Message dnsLookup = DNSLookup();
            dnsLookup.Content = Domain;
            SendMessage(dnsLookup);

            clientSocket.ReceiveTimeout = 5000;

            //TODO: [Receive and print DNSLookupReply from server]
            Message message = ReceiveMessage();
            return message;

        }
        catch (Exception e)
        {
            Console.WriteLine($"Error: {e.Message}");
            return null;
        }
    }
    private static Message HelloMessege()
    {
        Message helloMessage = new Message();
        helloMessage.MsgId = 1;
        helloMessage.MsgType = MessageType.Hello;
        helloMessage.Content = "Hello Server!";

        return helloMessage;
    }

    private static Message DNSLookup()
    {
        Message DNSLookup = new Message();
        DNSLookup.MsgId = random.Next(999999);
        DNSLookup.MsgType = MessageType.DNSLookup;
        DNSLookup.Content = "";
        return DNSLookup;
    }

    private static void SendMessage(Message message)
    {
        string messageString = JsonSerializer.Serialize(message);

        byte[] data = Encoding.UTF8.GetBytes(messageString);

        clientSocket.SendTo(data, serverEndPoint);
        Console.WriteLine($"============================================================");
        Console.WriteLine($"Message Send - MSG Type {message.MsgType}: {message.Content}");
        Console.WriteLine($"============================================================");
    }

    private static Message? ReceiveMessage()
    {
        try
        {
            int bytesReceived = clientSocket.ReceiveFrom(receiveBuffer, ref remoteEndPoint);
            string response = Encoding.UTF8.GetString(receiveBuffer, 0, bytesReceived);
            Message? message = JsonSerializer.Deserialize<Message>(response);
            Console.WriteLine($"============================================================");
            Console.WriteLine($"Received response - MSG Type {message.MsgType}: {message.Content}");
            Console.WriteLine($"============================================================");
            return message;
        }
        catch (SocketException ex) when (ex.SocketErrorCode == SocketError.TimedOut)
        {
            Console.WriteLine("No response received (timeout)");
        }      
        Thread.Sleep(messageInterval);
        return null;
    }
}