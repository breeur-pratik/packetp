Title: WICED getting started
Date: 2018-12-22 18:00
Category: IOT
Tags: IOT, WICED
Author:  Venkat Subbiah

### What is WICED

WICED stands for Wireless Internet Connectivity for Embedded Devices. It is a development system(IDE, SDK) that is used to develop software for Cypress(Formerly Broadcom IoT) based WiFi/Bluetooth devices that are paired  with a microcontroller.


### WICED Install

One of the first steps to get started with WICED is to install the SDK.  Below is a link to get the latest SDK’s and prior versions of the SDK. https://community.cypress.com/community/wiced-wifi/wiced-wifi-documentation.Recently Cypress has added some training videos. which  would be a good starting point for learning https://community.cypress.com/community/training-videos/


### Hardware Platform

You would also need a Hardware Platform that is capable of running the application from the SDK . Below are some recommendations. If your budget allows the 907 is a better choice.

CYW43907 Kit : The CYW43907 is a single-chip 802.11n dual-band (2.4GHz and 5GHz) Wi-Fi SoC with a 320MHz ARM Cortex-R4 MCU.

Here is a purchase link. https://www.mouser.com/new/cypress-semiconductor/cypress-wiced-cyw43907-kit/

 Avnet 4343W : One of the popular WICED hardware reference boards is the AVNET 4343w board. YOu could buy this of Amazon for 50USD. On Amazon.com Search for “AVNET BCM4343W” to find this board.  Below are some screenshots of the search.


### Documentation

WICED includes documentation with the SDK which has been generated from source using doxygen. The documentation is at $SDK_DIR/doc/API/index.html .After you install the SDK, the project explores shows the doc folder that contains the documentation.

Use a different versions of the SDK: 

When Cypress release a newer version of the SDK’s , you don’t need to resintall the IDE. You can just use the SDK source. Below blog show how to import a new SDK into the IDE.

https://community.cypress.com/community/wiced-wifi/wiced-wifi-forums/blog/2015/08/12/how-to-import-a-wiced-sdk-into-an-existing-wiced-eclipse-ide-2

Creating debug configuration after importing an SDK

https://community.cypress.com/community/wiced-wifi/wiced-wifi-forums/blog/2014/05/09/creating-andor-editing-debug-configurations

For copy paste convenience here are some strings used in the configuration.

On Mac

```
add-symbol-file build/eclipse_debug/last_built.elf 0x8000000
/Users/venkat/WICED/WICED-Studio-4.1/43xxx_Wi-Fi/tools/ARM_GNU/bin/OSX/arm-none-eabi-gdb
/Users/venkat/WICED/WICED-Studio-4.1/43xxx_Wi-Fi/build/eclipse_debug/last_built.elf.
${workspace_loc:/43xxx_Wi-Fi/build/eclipse_debug/last_built.elf}
${workspace_loc:/43xxx_Wi-Fi/tools/ARM_GNU/bin/OSX/arm-none-eabi-gdb}
${workspace_loc:/43xxx_Wi-Fi/build/eclipse_debug/last_built.elf}
${workspace_loc:/43xxx_Wi-Fi/build/eclipse_debug/last_built.elf}
```
