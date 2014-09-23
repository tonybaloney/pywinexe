$name = $args[0]
$path = "$env:ProgramData\Microsoft\Windows\Start Menu\Programs"
$start_menu = ls $path -Recurse -Include *$name*.lnk

ForEach($lnk in $start_menu){
   $shell = New-Object -ComObject WScript.Shell

   $name = $lnk.Name
   $path = $shell.CreateShortcut($lnk).targetpath   

   echo $path
}

