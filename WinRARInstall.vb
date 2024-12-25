' filepath: /Users/sonnystormes/Documents/pywinauto-demo/WinRARInstall.vb
Imports System
Imports System.Diagnostics
Imports System.Threading
Imports System.Windows.Automation

Module WinRARInstaller

    Sub Main()
        StartWinRARInstaller()
        AutomateInstallation()
    End Sub

    Sub StartWinRARInstaller()
        ' Start the WinRAR installer
        Process.Start("WinRAR-701.exe")
        Thread.Sleep(5000) ' Wait for the installer to open
    End Sub

    Sub AutomateInstallation()
        Try
            ' Find the WinRAR installer window
            Dim winRARWindow As AutomationElement = AutomationElement.RootElement.FindFirst(TreeScope.Children, New PropertyCondition(AutomationElement.NameProperty, "WinRAR Setup"))
            If winRARWindow IsNot Nothing Then
                Console.WriteLine("WinRAR window found")

                ' Click the "Next >" button
                ClickButton(winRARWindow, "Next >")

                ' Click the "Custom Setup" radio button
                ClickRadioButton(winRARWindow, "Custom Setup")

                ' Click the "Next >" button
                ClickButton(winRARWindow, "Next >")

                ' Click the "I accept the terms of the EULA" checkbox
                ClickCheckBox(winRARWindow, "I accept the terms of the EULA")

                ' Click the "Next" button
                ClickButton(winRARWindow, "Next")

                ' Enter "-custom" in the edit field
                EnterText(winRARWindow, "", "-custom")

                ' Click the "Install" button
                ClickButton(winRARWindow, "Install")
            Else
                Console.WriteLine("WinRAR window not found")
            End If

            ' Find the WinRAR Setup window
            Dim setupWindow As AutomationElement = AutomationElement.RootElement.FindFirst(TreeScope.Children, New PropertyCondition(AutomationElement.NameProperty, "WinRAR Setup"))
            If setupWindow IsNot Nothing Then
                Console.WriteLine("WinRAR Setup window found")

                ' Click the "OK" button
                ClickButton(setupWindow, "OK")

                ' Click the "Done" button
                ClickButton(setupWindow, "Done")
            Else
                Console.WriteLine("WinRAR Setup window not found")
            End If
        Catch ex As Exception
            Console.WriteLine("An error occurred: " & ex.Message)
        End Try
    End Sub

    Sub ClickButton(parent As AutomationElement, buttonName As String)
        Dim button As AutomationElement = parent.FindFirst(TreeScope.Descendants, New PropertyCondition(AutomationElement.NameProperty, buttonName))
        If button IsNot Nothing Then
            Dim invokePattern As InvokePattern = CType(button.GetCurrentPattern(InvokePattern.Pattern), InvokePattern)
            invokePattern.Invoke()
            Console.WriteLine("Clicked '" & buttonName & "' button")
            Thread.Sleep(2000) ' Wait for the next UI element to appear
        Else
            Console.WriteLine("Failed to find '" & buttonName & "' button")
        End If
    End Sub

    Sub ClickRadioButton(parent As AutomationElement, radioButtonName As String)
        Dim radioButton As AutomationElement = parent.FindFirst(TreeScope.Descendants, New PropertyCondition(AutomationElement.NameProperty, radioButtonName))
        If radioButton IsNot Nothing Then
            Dim selectionItemPattern As SelectionItemPattern = CType(radioButton.GetCurrentPattern(SelectionItemPattern.Pattern), SelectionItemPattern)
            selectionItemPattern.Select()
            Console.WriteLine("Clicked '" & radioButtonName & "' radio button")
            Thread.Sleep(2000) ' Wait for the next UI element to appear
        Else
            Console.WriteLine("Failed to find '" & radioButtonName & "' radio button")
        End If
    End Sub

    Sub ClickCheckBox(parent As AutomationElement, checkBoxName As String)
        Dim checkBox As AutomationElement = parent.FindFirst(TreeScope.Descendants, New PropertyCondition(AutomationElement.NameProperty, checkBoxName))
        If checkBox IsNot Nothing Then
            Dim togglePattern As TogglePattern = CType(checkBox.GetCurrentPattern(TogglePattern.Pattern), TogglePattern)
            togglePattern.Toggle()
            Console.WriteLine("Clicked '" & checkBoxName & "' checkbox")
            Thread.Sleep(2000) ' Wait for the next UI element to appear
        Else
            Console.WriteLine("Failed to find '" & checkBoxName & "' checkbox")
        End If
    End Sub

    Sub EnterText(parent As AutomationElement, editName As String, text As String)
        Dim edit As AutomationElement = parent.FindFirst(TreeScope.Descendants, New PropertyCondition(AutomationElement.NameProperty, editName))
        If edit IsNot Nothing Then
            Dim valuePattern As ValuePattern = CType(edit.GetCurrentPattern(ValuePattern.Pattern), ValuePattern)
            valuePattern.SetValue(text)
            Console.WriteLine("Entered '" & text & "' in the edit field")
            Thread.Sleep(2000) ' Wait for the next UI element to appear
        Else
            Console.WriteLine("Failed to find edit field to enter '" & text & "'")
        End If
    End Sub

End Module