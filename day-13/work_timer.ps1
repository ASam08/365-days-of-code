[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms")
$notificationFrequency = 30 # In minutes, not more than 60
$notificationWarning = 2 # In minutes

while ($true) {
    $waitCheck = (Get-Date).ToString("mm")   
    $multiplier = ([Math]::truncate($waitCheck/$notificationFrequency)) + 1

    if (($waitCheck) -ge (($notificationFrequency * $multiplier) - $notificationWarning)){
        $multiplier += 1
    } 

    $waitMinutes = ($multiplier * $notificationFrequency) - $notificationWarning

    if($waitMinutes -ge 60){
        $waitMinutes = $waitMinutes - 60
        $waitHours = 1
    }

    $waitTime = (Get-Date -Minute $waitMinutes -Second 0).AddHours($waitHours)
    $checkTime = Get-Date
    $waitSeconds = ($waitTime - $checkTime).TotalSeconds

    start-sleep -Seconds $waitSeconds

    $nearlyTime = $waitTime.ToString("HH:mm tt")
    $currentTime = (Get-Date).AddMinutes($notificationWarning).ToString("HH:mm tt")

    $objNotifyIcon = New-Object System.Windows.Forms.NotifyIcon
    $objNotifyIcon.Icon = [System.Drawing.SystemIcons]::Information
    $objNotifyIcon.BalloonTipTitle = "It's nearly $nearlyTime!"
    $objNotifyIcon.BalloonTipText = "It's currently $currentTime"
    $objNotifyIcon.Visible = $true
    $objNotifyIcon.ShowBalloonTip(10000) #Display for 10 seconds
    $objNotifyIcon.Dispose() #Clean up the icon after use
}