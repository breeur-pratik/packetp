Title: WICED : Managing repos
Date: 2018-12-26 18:00
Category: IOT
Tags: IOT, WICED
Author:  Venkat Subbiah

You have evaluated WICED and getting ready to build your own product with WICED. As you are developing code, you will possibly be developing these additional components

* libraries
* applications
* platforms.

Cypress does make releases of newer SDK’s quite often and usually doesn’t port fixes to older SDK’s. So it is better to manage your project so that you can easily move to newer SDK’s.

One way to manage this would be to have a stock version of the WICED SDK in one git repo and all your custom code in another repo. Here is how we mange it.

All our code is in a repository called pp_dev.

* pp_dev/pp_wiced_apps contains all our wiced application.
* pp_dev/pp_libraries contains all our WICED libraries.

Then we have link from WICED SDK repo to pp_dev repo.

```
VsMac2: ~/work/pp/wiced/wiced_6.2_mfi/WICED-Studio-6.2/43xxx_Wi-Fi/apps : ls -al
total 16
...
lrwxr-xr-x 1 venkat admin 42 Oct 25 07:52 pp_wiced_apps -> /Users/venkat/work/pp/pp_dev/pp_wiced_apps
drwxr-xr-x 71 venkat admin 2414 Jun 15 2018 snip
.....

VsMac2: ~/work/pp/wiced/wiced_6.2_mfi/WICED-Studio-6.2/43xxx_Wi-Fi/libraries : ls -al
total 8
drwxr-xr-x 16 venkat admin 544 Oct 25 07:52 .
drwxr-xr-x 31 venkat admin 1054 Nov 29 04:38 ..
drwxr-xr-x 11 venkat admin 374 Jun 15 2018 audio
...
drwxr-xr-x 8 venkat admin 272 Jun 15 2018 ota2_bt_service
lrwxr-xr-x 1 venkat admin 42 Oct 25 07:52 pp_libraries -> /Users/venkat/work/pp/pp_dev/pp_libraries/
drwxr-xr-x 16 venkat admin 544 Jun 15 2018 protocols
drwxr-xr-x 3 venkat admin 102 Jun 15 2018 scripting
.....
```
