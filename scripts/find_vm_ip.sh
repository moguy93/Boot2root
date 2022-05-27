#!/bin/bash
vBoxManage guestproperty enumerate Boot2Root
VBoxManage guestproperty get Boot2Root "/VirtualBox/GuestInfo/Net/0/V4/IP"
# works only if you have guest additions package installed in virtualBox
