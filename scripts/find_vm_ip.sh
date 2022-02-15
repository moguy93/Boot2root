#!/bin/bash
vBoxManage guestproperty enumerate boot2beroot
VBoxManage guestproperty get boot2beroot "/VirtualBox/GuestInfo/Net/0/V4/IP"
