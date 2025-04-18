---
aliases: 
cssclasses:
  - img-grid
  - embed-strict
  - wide-page
  - max
date: 2025-04-09
tags:
  - 2025/Apr
title: Powershell Guide
draft: "true"
---
# [[Powershell Guide]]

## Intent
I hardly use [[Powershell]] but it's a powerful tool to run a suite of commands in a Terminal.  

So with that in mind, I use a Powershell script to update my Blog!

This note is designed to explain what I've needed to learn with Powershell!

# Powershell Commands
clear - This will clear the terminal
Get-Help {cmdlet} - will list all help articles
ctrl + c - This will kill the current executed command
| - This will let you chain commands (like in Linux)
${var_name} = xyz - This stores a variable name that can be used in Powershell

# Execution Policy
#### Get-ExecutionPolicy    
This lets you know what your policy is

#### Set-ExecutionPolicy RemoteSigned  
This sets your policy **RemoteSigned** allows you to run your own scripts.

## Windows Powershell ISE
This is an IDE for writing PowerShell scripts
### Comments
This uses # just like in Python!
### Commands aka cmdlet
Verb-Noun format
"-" will auto complete with available commands
### Examples
Write-Host - This lets us print to the terminal 
"Hello World" | Out-File helloworld.txt - This will create a text file called helloworld.txt with "Hello World" inside of it
![Image Description](/images/Powershell%20Guide%201-1.png)



---
> [!createdat] Last updated on `="[[" + dateformat(this.file.mtime,"yyyy-MMM") + "]]"`.