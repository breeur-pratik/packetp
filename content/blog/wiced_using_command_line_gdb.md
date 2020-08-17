Title: WICED : Using command line gdb
Date: 2019-01-02 19:00
Category: IOT
Tags: WICED 
Author:  Venkat Subbiah


### Launch openocd in one console

```
"./tools/OpenOCD/OSX/openocd-all-brcm-libftdi" -s "./tools/OpenOCD/scripts" -f ./tools/OpenOCD/CYW9WCD1EVAL1.cfg -f ./tools/OpenOCD/stm32f4x.cfg -f ./tools/OpenOCD/stm32f4x-flash-app.cfg
```

### In another console launch gdb using

```
./tools/ARM_GNU/bin/OSX/arm-none-eabi-gdb
```

### Once you get to the gdb prompt use

```
(gdb) target remote localhost:3333
(gdb) monitor reset halt
(gdb) file build/snip.scan-BCM943364WCD1/binary/snip.scan-BCM943364WCD1.elf
(gdb) cont
```

### Below are logs from gdb and openocd

```
Venkats-MBP-9: ~/work/pp/wiced_6.00_pp/WICED-Studio-6.0/43xxx_Wi-Fi :
"./tools/OpenOCD/OSX/openocd-all-brcm-libftdi" -s "./tools/OpenOCD/scripts" -f
./tools/OpenOCD/CYW9WCD1EVAL1.cfg -f ./tools/OpenOCD/stm32f4x.cfg -f
./tools/OpenOCD/stm32f4x-flash-app.cfg
Open On-Chip Debugger 0.10.0-dev-00226-gb7080eca-dirty (2017-08-28-16:10)
Licensed under GNU GPL v2
For bug reports, read
   http://openocd.org/doc/doxygen/bugs.html
Info : only one transport option; autoselect 'jtag'
trst_and_srst separate srst_nogate trst_push_pull srst_push_pull connect_assert_srst
adapter speed: 1000 kHz
adapter_nsrst_delay: 100
jtag_ntrst_delay: 100
Warn : target name is deprecated use: 'cortex_m'
jtag_init
Warn : Using DEPRECATED interface driver 'ft2232'
Info : Consider using the 'ftdi' interface driver, with configuration files in interface/ftdi/...
Info : max TCK change to: 30000 kHz
Info : clock speed 1000 kHz
Info : JTAG tap: stm32f4xx.cpu tap/device found: 0x4ba00477 (mfg: 0x23b, part: 0xba00, ver: 0x4)
Info : JTAG tap: stm32f4xx.bs tap/device found: 0x06431041 (mfg: 0x020, part: 0x6431, ver: 0x0)
Warn : JTAG tap: stm32f4xx.bs       UNEXPECTED: 0x06431041 (mfg: 0x020, part: 0x6431, ver: 0x0)
Error: JTAG tap: stm32f4xx.bs  expected 1 of 1: 0x06413041 (mfg: 0x020, part: 0x6413, ver: 0x0)
Error: Trying to use configured scan chain anyway...
Warn : Bypassing JTAG setup events due to errors
Info : stm32f4xx.cpu: hardware has 6 breakpoints, 4 watchpoints
Info : JTAG tap: stm32f4xx.cpu tap/device found: 0x4ba00477 (mfg: 0x23b, part: 0xba00, ver: 0x4)
Info : JTAG tap: stm32f4xx.bs tap/device found: 0x06431041 (mfg: 0x020, part: 0x6431, ver: 0x0)
Warn : JTAG tap: stm32f4xx.bs       UNEXPECTED: 0x06431041 (mfg: 0x020, part: 0x6431, ver: 0x0)
Error: JTAG tap: stm32f4xx.bs  expected 1 of 1: 0x06413041 (mfg: 0x020, part: 0x6413, ver: 0x0)
Error: Trying to use configured scan chain anyway...
Warn : Bypassing JTAG setup events due to errors
Info : accepting 'gdb' connection on tcp/3333
Info : device id = 0x10006431
Info : flash size = 512kbytes
Warn : No RTOS could be auto-detected!
Info : JTAG tap: stm32f4xx.cpu tap/device found: 0x4ba00477 (mfg: 0x23b, part: 0xba00, ver: 0x4)
Info : JTAG tap: stm32f4xx.bs tap/device found: 0x06431041 (mfg: 0x020, part: 0x6431, ver: 0x0)
Warn : JTAG tap: stm32f4xx.bs       UNEXPECTED: 0x06431041 (mfg: 0x020, part: 0x6431, ver: 0x0)
Error: JTAG tap: stm32f4xx.bs  expected 1 of 1: 0x06413041 (mfg: 0x020, part: 0x6413, ver: 0x0)
Error: Trying to use configured scan chain anyway...
Warn : Bypassing JTAG setup events due to errors
stm32f4xx.cpu: target state: halted
target halted due to debug-request, current mode: Thread
xPSR: 0x01000000 pc: 0x080005a8 msp: 0x2001dcd0
Warn : No RTOS could be auto-detected!
Warn : No RTOS could be auto-detected!
Error: Unable to wipe mandatory variable: g_pendingtasks - address unknown
```

```
Venkats-MBP-9: ~/work/pp/wiced_6.00_pp/WICED-Studio-6.0/43xxx_Wi-Fi :
./tools/ARM_GNU/bin/OSX/arm-none-eabi-gdb
Python Exception &#60;type 'exceptions.ImportError'&#62; No module named gdb:

warning:
Could not load the Python gdb module from `/Users/lab/wiced/Wiced-Tool-Source/ARM_GNU/gdb-build/junk/python'.
Limited Python support is available from the _gdb module.
Suggest passing --data-directory=/path/to/gdb/data-directory.

GNU gdb (GDB) 7.7
Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later &#60;http://gnu.org/licenses/gpl.html&#62;
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "--host=x86_64-apple-darwin11.4.0 --target=arm-none-eabi".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
&#60;http://www.gnu.org/software/gdb/bugs/&#62;.
Find the GDB manual and other documentation resources online at:
&#60;http://www.gnu.org/software/gdb/documentation/&#62;.
For help, type "help".
Type "apropos word" to search for commands related to "word".
(gdb) Open On-Chip Debugger 0.10.0-dev-00226-gb7080eca-dirty (2017-08-28-16:10)
Licensed under GNU GPL v2
For bug reports, read
   http://openocd.org/doc/doxygen/bugs.html

(gdb)  target remote localhost:3333
Remote debugging using localhost:3333
0x080005a8 in ?? ()
(gdb) monitor reset halt
JTAG tap: stm32f4xx.cpu tap/device found: 0x4ba00477 (mfg: 0x23b, part: 0xba00, ver: 0x4)
JTAG tap: stm32f4xx.bs tap/device found: 0x06431041 (mfg: 0x020, part: 0x6431, ver: 0x0)
JTAG tap: stm32f4xx.bs       UNEXPECTED: 0x06431041 (mfg: 0x020, part: 0x6431, ver: 0x0)
JTAG tap: stm32f4xx.bs  expected 1 of 1: 0x06413041 (mfg: 0x020, part: 0x6413, ver: 0x0)
Trying to use configured scan chain anyway...
Bypassing JTAG setup events due to errors
stm32f4xx.cpu: target state: halted
target halted due to debug-request, current mode: Thread
xPSR: 0x01000000 pc: 0x080005a8 msp: 0x2001dcd0
(gdb) file build/snip.scan-BCM943364WCD1/binary/snip.scan-BCM943364WCD1.elf
A program is being debugged already.
Are you sure you want to change the file? (y or n) y
Reading symbols from build/snip.scan-BCM943364WCD1/binary/snip.scan-BCM943364WCD1.elf...done.
(gdb) cont
Continuing.
^C
Program received signal SIGINT, Interrupt.
platform_power_down_hook (sleep_ms=1135)
   at WICED/platform/MCU/STM32F4xx/peripherals/platform_mcu_powersave.c:333
333    }
(gdb) info threads
  Id   Target Id         Frame
* 1    Remote target     platform_power_down_hook (sleep_ms=1135)
   at WICED/platform/MCU/STM32F4xx/peripherals/platform_mcu_powersave.c:333
(gdb) bt
Python Exception &#60;type 'exceptions.ImportError'&#62; No module named gdb.frames:
#0  platform_power_down_hook (sleep_ms=1135)
   at WICED/platform/MCU/STM32F4xx/peripherals/platform_mcu_powersave.c:333
#1  0x08011508 in tx_low_power_enter ()
#2  0x08010e22 in __tx_ts_wait ()
Backtrace stopped: previous frame identical to this frame (corrupt stack?)
(gdb)
```
