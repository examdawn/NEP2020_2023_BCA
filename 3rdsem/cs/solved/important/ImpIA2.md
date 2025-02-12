# C#/Dotnet
# Important Questions, Internal Assessment 2
## Q1. Explain the If-Else statement in VB.NET and Give one example
If-Else, also known as If-Then-Else statements are used for basic conditional logic.
- It conditionally executes a group of statements, depending on the value of an expression.

Syntax:
```vb
If condition Then
    statements
ElseIf condition2 Then
     More Statements
Else
     else statements
End If
```
Just like if statement, it is always followed by "End If" to show that the if-else block is over.

Example: 
```vb
Dim n As Integer = 5

If n Mod 2 = 0 Then
    Console.WriteLine("Even")
Else
    Console.WriteLine("Odd")
End If
```

[Official Microsoft Docs](https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/if-then-else-statement)
## Q2. What is the purpose of Time control? 
The timer control is a looping control used to repeat any task in a given time interval. It is an important control used in Client-side and Server-side programming, also in Windows Services. It is used to execute an application after a specific amount of time. Once the timer is enabled, it generates a tick event handler to perform any defined task in its time interval property. [[1](https://www.javatpoint.com/vb-net-timer-control)]

## Q3. What is the use of Track bar control in VB.NET?
The Windows Forms TrackBar control (also sometimes called a "slider" control) is used for navigating through a large amount of information or for visually adjusting a numeric setting. 
- The TrackBar control has two parts: the thumb, also known as a slider, and the tick marks. 
    - The thumb is the part that can be adjusted. 
    - Its position corresponds to the Value property. 
    - The tick marks are visual indicators that are spaced at regular intervals. 
- The key properties of the TrackBar control are 
    - Value
    - TickFrequency is the spacing of the ticks
    - Minimum, and Maximum are the smallest and largest values that can be represented on the track bar

[Official Microsoft Docs](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/trackbar-control-overview-windows-forms)

## Q4. Write any two advantages of ADO.NET
ADO.NET(Active Data Objects .NET) is the database access framework used to connect to data sources like MS SQL Server, Microsoft Access, Oracle SQL, MySQL/MariaDB, SQLite, direct XML, etc

ADO.NET has many features like:
- Performance
    - ADO.NET works by using a disconnected data architecture 
    - This means it can scale easily without putting a huge load on the database server
    - Everything is handled Client-Side so it improves performance
- Scalability
    - Because it uses a disconnected data architecture, it can scale easily
    - Applications do not keep database locks for a longer time
    - It encourages programmers to use limited resources and allow concurrent use by design

[(GeeksForGeeks)](https://www.geeksforgeeks.org/introduction-to-ado-net/)
## Q5. Explain looping statements in VB.NET
In Visual Basic, loop statements are used to run code repeatedly while the condition is maintained.

There are 4 types of Loops:
- While Loops
    - While...End Loops repeat a set of statements as long as the given condition remains true
    - **Exit While** is functionally equivalent to break keyword from other languages and is used to exit the loop
    - **Continue While** is functionally equivalent to continue keyword and is used to skip the iteration and move to next iteration of the loop
    - Syntax:
        ```vb
        While condition
            statements
        End While
        ```
    - Example:
        ```vb
        While index <= 10
            Console.WriteLine(index.ToString)
            index += 1
        End While
        ```
- Do Loops
    - Do...Loop repeats a set of statements repeats code till the condition is no longer maintained
    - You can use either While or Until to specify condition, but not both. 
        - If you give neither, the loop continues until an Exit transfer control out of the loop.
    - Continue Do is functionally equivalent to continue keyword and is used to skip the iteration and move to next iteration of the loop
    - Exit Do is functionally equivalent to break keyword from other languages and is used to exit the loop
    - Syntax:
        ```vb
        Do { While | Until } condition
            statements
        Loop
        ```
    - Example:
        ```vb
        Do While index <= 10
            Console.WriteLine(index.ToString)
            index += 1
        Loop
        ```
- For Loops
    - For...Next repeats a set of statements repeats code till the condition is no longer maintained while maintaining a counter
    - **Exit For** is functionally equivalent to break keyword from other languages and is used to exit the loop
    - **Continue For** is functionally equivalent to continue keyword and is used to skip the iteration and move to next iteration of the loop
    - Syntax:
        ```vb
        For counter = start To End 
            statements
        Next
        ```
    - Example: 
        ```vb
        For index As Integer = 1 To 5
            Console.WriteLine(index.ToString)
        Next
        ```
- For Each Loops
    - For Each...Next repeats a set of statements repeats code for every element of the collection till the condition is no longer maintained while maintaining a counter
    - It is used for a collection of items like arrays
    - **Exit For** is functionally equivalent to break keyword from other languages and is used to exit the loop
    - **Continue For** is functionally equivalent to continue keyword and is used to skip the iteration and move to next iteration of the loop
    - Syntax:
        ```vb
        For Each element In group
            statements
        Next
        ```
    - Example: 
        ```vb
        Dim arr() As Integer = {1, 2, 3, 4, 5}
        For Each item As Integer In arr
            Console.WriteLine(item)
        Next
        ```

[Official Microsoft Docs](https://learn.microsoft.com/en-us/dotnet/visual-basic/programming-guide/language-features/control-flow/loop-structures)
## Q6. Write the difference between ADO and ADO.NET
 | ADO | ADO.NET |
 |---| --- |
| It is based on COM (Component Object Modelling). | It is a CLR (Common Language Runtime) based library. |
| It works only when data store is connected. | It does not needs active connection to access data from data store. |
| It has feature of locking. | It does not have feature of locking.
| It access and store data from data source by recordset object. | It access and store data from data source by dataset object. |
| XML integration is not feasible in ADO. | XML integration is feasible in ADO.NET. |
| In ADO, data is stored in binary form. | While in this, data is stored in XML. |
| It allow us to create client side cursors only. | It give us the choice of using weather client side and server side cursors. |
| It requires SQL JOINs and UNIONs to combine data from multiple tables in a single result table. | It uses DataRelational objects, for combining data from multiple tables without requiring JOINs and UNIONs. |
| It supports sequential access of rows in a RecordSet. | It allows completely non-sequential data access in DataSet through collection based hierarchy. |

[GeeksForGeeks](https://www.geeksforgeeks.org/difference-between-ado-and-ado-net/)

## Q7. Explain about combo box control and picture box control with an example
- **ComboBox control** - is used to display more than one item in a drop-down list. It is a combination of Listbox and Textbox in which the user can input only one item. Furthermore, it also allows a user to select an item from a drop-down list. [[1](https://www.javatpoint.com/vb-net-combobox-control)]
    
    ```VB
    Imports System.Windows.Forms
        Public Class Form1
            Private Sub Form1(sender As Object, e As EventArgs) Handles Me.Load
                Fruit.Items.Add("Banana")
                Fruit.Items.Add("Cherry")
                Fruit.Items.Add("Orange")
            End Sub

            Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
                Textbox1.Text = Fruit.Text
            End Sub
        End Class
    ```

- **PictureBox control** - is used to display the images on Windows Form. The PictureBox control has an image property that allows the user to set the image at runtime or design time.  [[1](https://www.javatpoint.com/vb-net-picturebox-control)]
    
    ```VB
        Public Class Picturebx  
        Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click  
            'Dim Str As String = "C:\Users\AMIT YADAV\Desktop\"  
            PictureBox1.Image = Image.FromFile("C:\Users\AMIT YADAV\Desktop\jtp2.png")  
            PictureBox1.SizeMode = PictureBoxSizeMode.StretchImage  
            PictureBox1.Height = 250  
            PictureBox1.Width = 400  
            Label1.Visible = False  
        End Sub  
        Private Sub Picturebx_Load(sender As Object, e As EventArgs) Handles MyBase.Load  
            Me.Text = "javaTpoint.com" 'Set the title name for the form  
            Button1.Text = "Show"  
            Label1.Text = "Click to display the image"  
            Label1.ForeColor = ForeColor.Green  
        End Sub  
    End Class  
    ```
    
[JavaTPoint](https://www.javatpoint.com/vb-net-picturebox-control)
## Q8. Explain Data reader and Data adapter in ADO.NET

#### DataReader
`DataReader` is a forward-only, read-only cursor used to retrieve a stream of data from a database. 
- It is designed for high performance and is ideal for scenarios where you need to read data quickly and efficiently.
- Key Features:

    - ***Forward-Only***:
        - The `DataReader` can only traverse the data in a forward direction. Once you read a row, you cannot go back.
    - ***Read-Only***:
        - You cannot update or modify the data while using a `DataReader`. It is strictly for reading data.
    - ***Connection-Based***:
        - The `DataReader` requires an open connection to the database while reading data. This means that the connection must remain open for the duration of the read operation.
    - ***Lightweight***:
        - Since it uses less memory and resources compared to other data retrieval methods, it is faster and more efficient for large datasets.
---
#### DataAdapter
`DataAdapter` serves as a bridge between a DataSet and a data source. 
- It is used to fill a DataSet with data and to update the data source with changes made in the DataSet. 
- It provides a more flexible way to work with data compared to `DataReader`.
- Key Features:
    - ***Disconnected Architecture***: 
        - The `DataAdapter` allows you to work with data in a disconnected manner. 
        - You can fill a DataSet with data and then close the connection, allowing you to work with the data offline.
    - ***Supports Multiple Tables***:
        -  A `DataAdapter` can fill multiple tables in a DataSet and can also manage relationships between those tables.
    - ***CRUD Operations***: 
        - It can be used to perform Create, Read, Update, and Delete (CRUD) operations. 
        - You can update the data source with changes made to the DataSet using the Update method.
    - ***DataSet Integration***: 
        - The `DataAdapter` works with DataSet, allowing you to store data in memory and manipulate it without needing to constantly connect to the database.

## Q9. Explain any 4 tools and its properties from toolbox of VB.NET

#### 1. TextBox
**Description**: A `TextBox` control allows users to input and edit text. It is commonly used for forms where user input is required.

**Properties**:
- **Text**: Gets or sets the text displayed in the `TextBox`. This is the most commonly used property.
- **MaxLength**: Sets the maximum number of characters that the user can enter. This is useful for limiting input, such as for usernames or passwords.
- **Multiline**: A Boolean property that, when set to `True`, allows the `TextBox` to accept multiple lines of text. This is useful for comments or descriptions.
- **ReadOnly**: When set to `True`, the user cannot change the text in the `TextBox`, making it useful for displaying information that should not be edited.

**Practical Use**: A `TextBox` is often used in forms for input fields like name, email, or password. For example, in a login form, you would typically have two `TextBox` controls for the username and password.

---

#### 2. ComboBox
**Description**: A `ComboBox` combines a drop-down list with an editable text box, allowing users to either select an item from a list or enter a custom value.

**Properties**:
- **Items**: A collection that holds the items in the `ComboBox`. You can add or remove items dynamically at runtime.
- **SelectedIndex**: Gets or sets the zero-based index of the currently selected item. This is useful for retrieving the user's selection.
- **DropDownStyle**: Determines how the `ComboBox` behaves. Options include `DropDown`, `DropDownList`, and `Simple`. `DropDownList` prevents users from entering custom values.
- **AutoCompleteMode**: Allows the `ComboBox` to suggest items as the user types, enhancing user experience.

**Practical Use**: A `ComboBox` is often used for selecting options from a predefined list, such as selecting a country from a list of countries in a registration form. It can also allow users to input custom values if needed.

---

#### 3. ListBox
**Description**: A `ListBox` displays a list of items from which the user can select one or more items. It is useful for presenting a collection of options.

**Properties**:
- **Items**: Similar to the `ComboBox`, this property holds the collection of items in the `ListBox`.
- **SelectionMode**: Determines how selections are made within the `ListBox`. Options include `One` (single selection), `MultiSimple`, and `MultiExtended` (multiple selections).
- **SelectedItems**: Returns a collection of the currently selected items, allowing you to easily access user selections.
- **HorizontalScrollbar**: A Boolean property that, when set to `True`, enables a horizontal scrollbar if the items exceed the width of the `ListBox`.

**Practical Use**: A `ListBox` is often used to display options for selection, such as a list of available products in an e-commerce application. Users can select multiple items (e.g., multiple products) to add to their cart.

---

#### 4. PictureBox
**Description**: A `PictureBox` control is used to display images in a Windows Forms application. It can show bitmaps, icons, or other types of images.

**Properties**:
- **Image**: Gets or sets the image displayed in the `PictureBox`. You can load images from files, resources, or streams.
- **SizeMode**: Determines how the image is displayed within the `PictureBox`. Options include `Normal`, `StretchImage`, `AutoSize`, and `CenterImage`. This allows you to control how the image fits within the control.
- **BackColor**: Sets the background color of the `PictureBox`, which can be useful if the image does not fill the entire control.
- **BorderStyle**: Specifies the border style of the `PictureBox`, which can be set to `None`, `FixedSingle`, or `Fixed3D`.

**Practical Use**: A `PictureBox` is commonly used in applications that require image display, such as a photo viewer or an application that showcases product images. For instance, in a gallery application, each `PictureBox` can display a different image, allowing users to browse through a collection.

## Q10. Explain subroutine and functions with the help of example
| Parameters | Sub Procedures | Functions |
|------------|----------------|-----------|
| 1          | A subprocedure is not associated with an event. | A function is also not associated with an event. |
| 2          | A subprocedure is called whenever it is required to perform certain tasks. It returns control to the calling code after performing a task. | A function is called whenever a value is required to be returned to the calling code after performing a task. |
| 3          | A subprocedure does not return a value to the calling code. | Functions return a value to the calling code. |
| 4          | A subprocedure cannot be used with an expression. | Functions are used in an expression. |
| 5          | A subprocedure helps to make the code readable, and easy to modify and debug. | In functions, it is not easy to modify and debug the code. |
| 6          | A subprocedure is a generalized type of function. | A function is a specific type of procedure. |
| 7          | A subprocedure is declared with the keyword Sub. | A function is declared with the keyword Function. | 

[[1](https://www.geeksforgeeks.org/sub-procedure-vs-function-in-vb-net/)]

- Example for Subroutine:
    ```VB
    Class Program
        Sub Main()
            DisplayMessage()
        End Sub

        Sub DisplayMessage()
            Console.WriteLine("Hello, this is a subroutine!")
        End Sub
    End Class
    ```

- Example for Function
    ```VB
    Class Program
        Sub Main()
            Dim result As Integer
            result = AddNumbers(5, 10)
            Console.WriteLine("The sum is: " & result)
            Console.ReadLine()
        End Sub

        Function AddNumbers(a As Integer, b As Integer) As Integer
            Return a + b
        End Function
    End Class
    ````

## Q11. Explain the architecture of ADO.NET
ADO.NET has two main components that are used for accessing and manipulating data are the .NET Framework data provider and the DataSet. [[1](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/ado-net-architecture)]
- **.NET Framework data provider** - These are the components that are designed for data manipulation and fast access to data. It provides various objects such as Connection, Command, DataReader and DataAdapter that are used to perform database operations. 
- **DataSet** - It is used to access data independently from any data resource. DataSet contains a collection of one or more DataTable objects of data.  [[2](https://www.javatpoint.com/ado-net-introduction)]

## Q12. What is Data set and Data Provider? 
- Already Answered

## Q13. What is docking and undocking in visual studio?
Docking and undocking in Visual Studio for Windows Forms refers to the ability to arrange controls within a form. Docking allows a control to attach itself to one of the edges of its parent container, automatically resizing to fill the available space. This is useful for creating layouts that adapt to different form sizes and orientations. Undocking, on the other hand, allows a control to be separated from its parent container, enabling it to float freely or be moved to another location, such as a different monitor. [[1](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/how-to-dock-and-anchor?view=netdesktop-9.0)]

## Q14. Explain Task bar and Progress bar controls of VB.NET
- **Progress Bar** - It represents a Windows progress bar control. It is used to provide visual feedback to your users about the status of some task. It shows a bar that fills in from left to right as the operation progresses. Similar to what we all seen when downloading or sharing any content.

- **Taskbar** - TODO

## Q15. Explain the steps to create a simple form using VB.NET
To create a Visual Basic application project. The project type comes with all the template files that you need.
- Step 1: Open Visual Studio.
- Step 2: On the start window, choose Create a new project.
- Step 3: On the Create a new project window, select the Windows Forms App (.NET Framework) template for Visual Basic.
- Step 4: In the Configure your new project window, enter project_name as the Project name. Then, select Create.
- Step 5: On the left side of the Visual Studio IDE, select the Toolbox tab. If you don't see it, select View > Toolbox from the menu bar or Ctrl+Alt+X. 
    - Select the Label control in the Toolbox window, and then drag it onto the form.
    - In the Properties window, change the text from Label1 to Null, and then press Enter.
    - Select the Button control and then drag it onto the form.
    - In the Properties window, change the text from Button1 to Submit, and then press Enter.
- Step 6: Now add the code by double clicking the button control.
    - ```VB
        Public Class Form1
            Private Sub Button1(sender As Object, e As EventArgs) Handles Button1.Click
                label1.Text = "Hello World!"
            End Sub
        End Class
      ```
- Step 7: Now your application is ready to build and run.
- Step 8: Select Start to run the application. [It will handle both the building and running by itself.]  [[1](https://learn.microsoft.com/en-us/visualstudio/ide/create-a-visual-basic-winform-in-visual-studio?view=vs-2022)]

## Q16. Explain VB.NET Conditional and looping statements with a suitable example
[Conditional Statements are already answered in Q1.](#q1-explain-the-if-else-statement-in-vbnet-and-give-one-example)
- Example for Conditional Statement
    ```VB
    Class Genshin
        ' Declaration of variable str
        Dim str As String = "Impact"
        Sub Main()
        ' if str equal to "Impact", below Statement will be executed.
        If str = "Impact" Then
            Console.WriteLine("Get Help!")
        End If
        Console.WritLine("press any key to TOUCH GRASS?")
        Console.ReadKey()
        End Sub
    End Class
    ```
[Looping Statements are already answered in Q5.](#q5-explain-looping-statements-in-vbnet)
- Example for Looping Statement
    ```VB  
    Class Pablo
        Sub Main()
            ' 'vbCrLf' is used to jump in the next line just like \n in C.
            Console.Write(" The number starts from 1 to 10 " & vbCrLf)
            For i As Integer = 1 To 10 Step 1
                ' if the condition is true, the following statement will be executed
                Console.WriteLine(" Number is {0} ", i)
                ' after completion of each iteration, next will update the variable counter
            Next
            Console.WriteLine(" Press any key to BE FREEEE!")
            Console.ReadKey()
        End Sub
    End Class
    ```

## Q17. Explain Exception Handling in C# with example syntax
An exception is a problem that arises during the execution of a program. A C# exception is a response to an exceptional circumstance that arises while a program is running, such as an attempt to divide by zero. Exceptions provide a way to transfer control from one part of a program to another. C# exception handling is built upon four keywords: try, catch, finally, and throw.
- **try** − A try block identifies a block of code for which particular exceptions is activated. It is followed by one or more catch blocks.
- **catch** − A program catches an exception with an exception handler at the place in a program where you want to handle the problem. The catch keyword indicates the catching of an exception.
- **finally** − The finally block is used to execute a given set of statements, whether an exception is thrown or not thrown. For example, if you open a file, it must be closed whether an exception is raised or not.
- **throw** − A program throws an exception when a problem shows up. This is done using a throw keyword.  [[1](https://www.tutorialspoint.com/csharp/csharp_exception_handling.htm)]

Syntax:
```C#
try {
   // statements causing exception
} catch( ExceptionName e1 ) {
   // error handling code
} catch( ExceptionName e2 ) {
   // error handling code
} finally {
   // statements to be executed
}
```