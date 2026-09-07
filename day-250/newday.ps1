# Work out how many days into the year it is
$day = [int](Get-Date).DayOfYear

# Create a new folder for today
$folderName = "day-$day"
mkdir $folderName

# Create a new markdown file for today from the template
$templatePath = "template\main.md"
$newFilePath = "$folderName/day-$day.md"
Copy-Item -Path $templatePath -Destination $newFilePath
$content = Get-Content -Path $newFilePath -Raw

$content = $content -replace "{{DAY_NUMBER}}", $day

$title = Read-Host "What is today's Title? Enter for blank"
$content = $content -replace "{{TITLE}}", $title

$addTimetableFooter = Read-Host "Do you want to add a footer note? (y/n)"
if ($addTimetableFooter -eq "y") {
    $footerSelector = Read-Host "Which footer do you want to add?`n(1) Timetable Footer`n(2) Wardrobe Footer`n"
    if ($footerSelector -eq "1") {
        $timetableFooter = Get-Content -Path "template\timetable-footer.md" -Raw
        $timetableFooter = "`n" + $timetableFooter + "`n"
        $content += $timetableFooter
    } elseif ($footerSelector -eq "2") {
        $wardrobeFooter = Get-Content -Path "template\wardrobe-footer.md" -Raw
        $wardrobeFooter = "`n" + $wardrobeFooter + "`n"
        $content += $wardrobeFooter
    }
}
$content | Out-File -FilePath $newFilePath -Encoding UTF8