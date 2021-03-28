$path = "C:\Users\ur\Downloads\msg.txt"
[System.Convert]::ToBase64String((Get-Content $path -Encoding Byte))