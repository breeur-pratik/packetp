Title: Running WiFi example on CY8CPROTO_062_4343W
Date: 2019-05-19 18:00
Category: IOT
Tags: IOT, WICED, NETWORKING, CY8CPROTO_062_4343W
Author:  Venkat Subbiah


At Packet Path we have worked on several projects using Cypress WiFi/BT chips. One of the popular chip is 4343W. I am excited that a driver for 4343W is available in mbed. 4343W is the chip that’s on the CY8CPROTO_062_4343W kit. Below are instructions to try out the mbed-os-example-wifi on the kit.

If mbed detect doesn’t detect your board, you would need to get the fw-loader program from:
https://github.com/cypresssemiconductorco/Firmware-loader/releases

And run the commad
```
fw-loader.exe --update-kp3
```

Import the mbed-os-example-wifi example using . The cool thing about mbed is that this same program will work with other boards that have WiFi module. I had used this previously with an STM32 board

```
mbed import mbed-os-example-wifi
```

Configure the SSID and password used to connect, by editing mbed_app.json

```
drwxr-xr-x   7 venkat  admin   238 Nov  9  2018 wifi-ism43362
 (embed) VsMac2: ~/work/pp/pp_dev/mbed/snips/mbed-os-example-wifi : cat mbed_app.json 
 {
     "config": {
         "wifi-ssid": {
             "help": "WiFi SSID",
             "value": "\"VSG1\""
         },
         "wifi-password": {
             "help": "WiFi Password",
             "value": "\"YOUR_PASSWORD\""
         }
     },
     "target_overrides": {
         "*": {
             "platform.stdio-convert-newlines": true
         }
     }
 }
```

Then compile and load the program to the device using.

```
mbed compile -f -m CY8CPROTO_062_4343W -t GCC_ARM
```

Here are some other links that talk about the board.

1. https://iotexpert.com/2019/02/09/cypress-mbed-os/
2. https://community.cypress.com/community/modustoolbox/blog/2019/03/27/a-wifi-scanner-using-the-mbed-modustoolbox-flow


Logs from compiling are

```
(embed) VsMac2: ~/work/pp/pp_dev/mbed/try/mbed-os-example-wifi : mbed compile -f -m CY8CPROTO_062_4343W -t GCC_ARM
 [mbed] Auto-installing missing Python modules…
 [Warning] @,: Compiler version mismatch: Have 7.3.1; expected version >= 6.0.0 and < 7.0.0
 Building project mbed-os-example-wifi (CY8CPROTO_062_4343W, GCC_ARM)
 Scan: mbed-os-example-wifi
 Compile [  0.1%]: except.S
 Compile [  0.2%]: mbed_tz_context.c
 Compile [  0.3%]: rf_configuration.c
 Compile [  0.5%]: MCR20Drv.c
 Compile [  0.6%]: mbed_fault_handler.c
 Compile [  0.7%]: at24mac.cpp
 Compile [  0.8%]: NanostackRfPhyMcr20a.cpp
 Compile [  0.9%]: AnalogIn.cpp
 Compile [  1.0%]: NanostackRfPhyAtmel.cpp
 Compile [  1.1%]: NanostackRfPhys2lp.cpp
 …
 …
 Compile [ 99.1%]: sleep_api.c
 Compile [ 99.2%]: cy_usbfs_dev_drv_io_dma.c
 Compile [ 99.3%]: rtc_api.c
 Compile [ 99.4%]: trng_api.c
 Compile [ 99.5%]: pwmout_api.c
 Compile [ 99.7%]: serial_api.c
 Compile [ 99.8%]: us_ticker.c
 Compile [ 99.9%]: spi_api.c
 Compile [100.0%]: default_wifi_interface.cpp
 Link: mbed-os-example-wifi
 Elf2Bin: mbed-os-example-wifi
 …
 …
 Total Static RAM memory (data + bss): 26576(+26576) bytes
 Total Flash memory (text + data): 555581(+555581) bytes
 Image: ./BUILD/CY8CPROTO_062_4343W/GCC_ARM/mbed-os-example-wifi.hex

```

Logs from the serial console of the device when running the mbed-os-example-wifi.

```
WiFi example
 Mbed OS version 5.12.3
 Scan:
 Network: subbs_in secured: WPA2 BSSID: E4:95:6E:41:9f:36 RSSI: -60 Ch: 1
 Network: subbs_2GEXT secured: WPA2 BSSID: A0:4:60:2a:1b:c4 RSSI: -23 Ch: 1
 Network:  secured: WPA2 BSSID: 8A:2A:A8:3:bc:a9 RSSI: -80 Ch: 1
 Network: SBG secured: WPA2 BSSID: 80:2A:A8:3:bc:86 RSSI: -63 Ch: 1
 Network: SBG secured: WPA2 BSSID: 80:2A:A8:3:bc:a9 RSSI: -76 Ch: 1
 Network: subbs_tm secured: WPA2 BSSID: E8:8D:28:60:78:29 RSSI: -52 Ch: 6
 Network: ParkPaiz secured: WPA2 BSSID: 10:86:8C:20:9a:6 RSSI: -68 Ch: 6
 Network: xfinitywifi secured: No:e Bc6:75 RSSI: -61 Ch: 11
 Network: VSGo secured: None BSSID: BC:EE:7B:dd:d3:42 RSSI: -56 Ch: 11
 Network: ATT4z5JAX7 secured: WPA2 BSSID: F8:2C:18:70:db:72 RSSI: -91 Ch: 11
 13 networks available.
 Connecting to VSG1…
 Success
 MAC: 00:9d:6b:67:53:7e
 IP: 192.168.2.56
 Netmask: 255.255.255.0
 Gateway: 192.168.2.1
 RSSI: -57
 Sending HTTP request to www.arm.com…
 sent 58 [GET / HTTP/1.1]
 recv 64 [HTTP/1.1 200 OK]
 Done
```
