class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit

    def inches(self):
        if self.unit == "feet":
            return self.length * 12
        elif self.unit == "yards":
            return self.length * 36
        elif self.unit == "miles":
            return self.length * 63360
        elif self.unit == "kilometers":
            return self.length * 39370.1
        elif self.unit == "meters":
            return self.length * 39.3701
        elif self.unit == "centimeters":
            return self.length * 0.393701
        elif self.unit == "millimeters":
            return self.length * 0.0393701
        else:
            return self.length

    def feet(self):
        if self.unit == "inches":
            return self.length / 12
        elif self.unit == "yards":
            return self.length * 3
        elif self.unit == "miles":
            return self.length * 5280
        elif self.unit == "kilometers":
            return self.length * 3280.84
        elif self.unit == "meters":
            return self.length * 3.28084
        elif self.unit == "centimeters":
            return self.length * 0.0328084
        elif self.unit == "millimeters":
            return self.length * 0.00328084
        else:
            return self.length

    def yards(self):
        if self.unit == "inches":
            return self.length / 36
        elif self.unit == "feet":
            return self.length / 3
        elif self.unit == "miles":
            return self.length * 1760
        elif self.unit == "kilometers":
            return self.length * 1093.61
        elif self.unit == "meters":
            return self.length * 1.09361
        elif self.unit == "centimeters":
            return self.length * 0.0109361
        elif self.unit == "millimeters":
            return self.length * 0.00109361
        else:
            return self.length

    def miles(self):
        if self.unit == "inches":
            return self.length / 63360
        elif self.unit == "feet":
            return self.length / 5280
        elif self.unit == "yards":
            return self.length / 1760
        elif self.unit == "kilometers":
            return self.length / 1.609344
        elif self.unit == "meters":
            return self.length / 1609.344
        elif self.unit == "centimeters":
            return self.length / 160934.4
        elif self.unit == "millimeters":
            return self.length / 1.609344e6
        else:
            return self.length

    def kilometers(self):
        if self.unit == "inches":
            return self.length * 0.0000254
        elif self.unit == "feet":
            return self.length * 0.0003048
        elif self.unit == "yards":
            return self.length * 0.0009144
        elif self.unit == "miles":
            return self.length * 1.609344
        elif self.unit == "meters":
            return self.length / 1000
        elif self.unit == "centimeters":
            return self.length / 100000
        elif self.unit == "millimeters":
            return self.length / 1e6
        else:
            return self.length

    def meters(self):
        if self.unit == "inches":
            return self.length * 0.0254
        elif self.unit == "feet":
            return self.length * 0.3048
        elif self.unit == "yards":
            return self.length * 0.9144
        elif self.unit == "miles":
            return self.length * 1609.344
        elif self.unit == "kilometers":
            return self.length * 1000
        elif self.unit == "centimeters":
            return self.length / 100
        elif self.unit == "millimeters":
            return self.length / 1000
        else:
            return self.length

    def centimeters(self):
        if self.unit == "inches":
            return self.length * 2.54
        elif self.unit == "feet":
            return self.length * 30.48
        elif self.unit == "yards":
            return self.length * 91.44
        elif self.unit == "miles":
            return self.length * 160934.4
        elif self.unit == "kilometers":
            return self.length * 100000
        elif self.unit == "meters":
            return self.length * 100
        elif self.unit == "millimeters":
            return self.length / 10
        else:
            return self.length

    def millimeters(self):
        if self.unit == "inches":
            return self.length * 25.4
        elif self.unit == "feet":
            return self.length * 304.8
        elif self.unit == "yards":
            return self.length * 914.4
        elif self.unit == "miles":
            return self.length * 1.609344e6
        elif self.unit == "kilometers":
            return self.length * 1e6
        elif self.unit == "meters":
            return self.length * 1000
        elif self.unit == "centimeters":
            return self.length * 10
        else:
            return self.length
