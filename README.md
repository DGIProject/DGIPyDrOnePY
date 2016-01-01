# DGIPyDrOnePY
Scripts for Raspberry Pi to pilot a drone.

# Start
- Change path to PY folder in statupDrone and choose communication system between python and nodejs
- Copy startupDrone in init.d folder : `cd /etc/init.d` and `cp "PYFOLDER"/startupDrone startupDrone`
- Add this script in start of OS : `update-rc.d startupDrone defaults`
- Restart your OS and try : `sudo reboot`
