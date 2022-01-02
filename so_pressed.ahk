if A_Args.Length() < 1
{
    MsgBox % "This script requires at least 1 parameters, but only " A_Args.Length() " were given!"
    ExitApp
}
#IfWinExist Roblox
SendInput, {%1% down}
Sleep, 250
SendInput, {%1% up}
return
ExitApp