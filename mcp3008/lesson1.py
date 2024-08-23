import gpiozero as zero
from time import sleep

if __name__ == "__main__":
    mcp3008_7 = zero.MCP3008(7);
    mcp3008_6 = zero.MCP3008(6);
    while True:
        print("the channel 7 光敏電阻:{:.2f}".format(mcp3008_7.value));
        print("the channel 6 可變電阻:{:.2f}".format(mcp3008_6.value))
        sleep(1)