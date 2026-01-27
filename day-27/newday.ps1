# Work out how many days into the year it is
$day = ((Get-Date) - (Get-Date -Year (Get-Date).Year -Month 1 -Day 1)).Days + 1

# Create a new folder for today
$folderName = "day-$day"
mkdir $folderName

# Create a new markdown file for today from the template
$templatePath = "template\main.md"
$newFilePath = "$folderName/day-$day.md"
Copy-Item -Path $templatePath -Destination $newFilePath
$content = Get-Content -Path $newFilePath -Raw

$content = $content -replace "{{DAY_NUMBER}}", $day

$addTimetableFooter = Read-Host "Do you want to add the timetable footer note? (y/n)"
if ($addTimetableFooter -eq "y") {
    $timetableFooter = Get-Content -Path "template\timetable-footer.md" -Raw
    $timetableFooter = "`n" + $timetableFooter + "`n"
    $content += $timetableFooter
}
$content | Out-File -FilePath $newFilePath -Encoding UTF8