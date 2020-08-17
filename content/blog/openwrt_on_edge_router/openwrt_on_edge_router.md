Title: Steps to compile and run OpenWRT on Edge Router
Date: 2019-01-02 18:00
Category: NETWORKING
Tags: OpenWRT, Edge Router
Author:  Venkat Subbiah


### Open to access USB drive

Need to open up the Edge Router to access the USB drive. It needs to be . Below is picture after opening it up. Be careful when unplugging the USB drive. Hold on to the USB connector, so that there is not much pull on the connector

![Photo]({attach}edge_router.jpg)


### Get Source

Clone using

```
git://git.openwrt.org/14.07/openwrt.git
```


### Build

From the top dir run “make menuconfig and set target to be Octeon. Pictures showing top dir and Target selection below.


![Photo]({attach}dir_list.png)

![Photo]({attach}menu_config.png)


### Partition

The partition of the USB drive looked like below. I probably had partitioned this before. If it doesn’t look like below, you want to use fdisk to partition the USB drive.

```
Disk /dev/sdg: 3880 MB, 3880452096 bytes
120 heads, 62 sectors/track, 1018 cylinders, total 7579008 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
Disk identifier: 0xe9ad0200
Device Boot Start End Blocks Id System 
/dev/sdg1 2048 292863 145408 c W95 FAT32 (LBA)
/dev/sdg2 292864 3710975 1709056 83 Linux
```


### Images

After the build completes there will be image in in ./bin/octeon directory.

```
cp kernel  /media/venkat/0243-8F11/vmlinux
```

Copy the kernel to the first partition

```
cp kernel  /media/venkat/0243-8F11/vmlinux
```

Extract rootfs to the second partition. Be very careful hre and choose the right drive and partition for of

```
sudo dd if=./root of=/dev/sdg2 bs=1M
```

Plugin in the USB and boot.
