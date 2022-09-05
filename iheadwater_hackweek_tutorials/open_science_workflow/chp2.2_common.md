# 2.2 管理目录和文件的 Bash 命令

:::{note}
本节正在编辑中……
:::

在前面关于终端会话的部分中，您了解到终端会显示一个提示，提示您Bash正在等待输入。

$bash  

回想一下，根据您的计算机设置，您可能会看到不同的字符作为提示和/或提示之前的附加信息，例如您在计算机文件结构中的当前位置（即您当前的工作目录）。

键入命令（来自本教科书或其他来源）时，请勿键入美元符号（或其他字符提示符）。只键入它后面的命令。

注意：在本页的示例中，提示符后面的缩进行不以美元符号$开头是命令的输出。以下命令在您的计算机上的结果会略有不同，具体取决于您的操作系统以及您自定义文件系统的方式。

下面是一些常用的bash命令，让我们来操作下吧。

## 1. 打印当前工作目录 ( pwd)

您当前的工作目录是执行命令的目录。它通常打印为目录的完整路径（意味着您可以看到父目录）。

要打印当前工作目录的名称，请使用命令pwd。

$ pwd    
   
   /users/jpalomino  
由于这是您Bash在此会话中执行的第一个命令，因此结果pwd是您的主目录的完整路径。主目录是您每次启动新Bash会话时将位于的默认目录。

Windows 用户：请注意，Terminal使用正斜杠 ( /) 来指示路径中的目录。这与使用反斜杠 ( \) 指示路径中的目录的 Windows 文件资源管理器不同。

## 2. 更改当前工作目录 ( cd)

通常，您可能想要更改当前工作目录，以便可以访问不同的子目录和文件。

要更改目录，请使用cd后跟目录名称的命令（例如cd downloads）。然后，您可以再次打印当前工作目录以检查新路径。

例如，您可以将工作目录更改为主documents目录下的现有目录，然后检查当前工作目录是否已更新。

$cd documents  

$pwd  
    /users/jpalomino/documents  
您可以使用该命令返回任何当前目录的父目录cd ..，因为当前工作目录的完整路径可以被Bash.

$ cd ..    

$ pwd  
    /users/jpalomino  
/users/jpalomino您也可以随时使用命令cd ~（称为波浪号的字符）返回您的主目录（例如）。

$ cd ~  

$ pwd  
    /users/jpalomino
    
    
    
## 3.创建新目录 ( mkdir)


创建新目录的第一步是导航到您希望成为该新目录的父目录的目录，使用cd.

然后，使用命令mkdir后跟您要为新目录命名的名称（例如mkdir directory-name）。

例如，您可以在documentscalled下创建一个新目录assignments。然后，您可以导航到名为 的新目录assignments，并打印当前工作目录以检查新路径。

$ cd documents

$ mkdir assignments

$ cd assignments

$ pwd
   
   /users/jpalomino/documents/assignments

请注意，mkdir命令没有输出。此外，由于assignments提供 toBash作为相对路径（即，没有前导斜杠或附加路径信息），documents默认情况下在当前工作目录（例如 ）中创建新目录。

## 4. 打印文件和子目录列表 ( ls)



要查看当前工作目录中所有子目录和文件的列表，请使用命令ls。

$ cd ~

$ pwd
    
/users/jpalomino

$ ls 
    
addresses.txt    documents    downloads    grades.txt    

在上面的示例中，ls打印了主目录的内容，其中包含名为 and 的子目录和名为anddocuments的downloads文件。addresses.txtgrades.txt

您可以继续将当前工作目录更改为子目录，例如documents并打印所有文件和子目录的新列表以查看新创建的assignments目录。

$ cd documents

$ ls    
    
assignments  

assignments也可以在叫下新建一个子目录homeworks，然后列出目录的内容就assignments可以看到新创建的了homeworks。

$ cd assignments

$ mkdir homeworks

$ ls    
    
homeworks  

## 5. 删除文件 ( rm)

要删除特定文件，您可以使用命令rm后跟要删除的文件的名称（例如rm filename）。

例如，您可以删除addresses.txt主目录下的文件。

$ pwd

/users/jpalomino

$ ls 
    
addresses.txt    documents    downloads    grades.txt 

$ rm addresses.txt

$ ls 
    
documents    downloads    grades.txt

## 6.删除目录 ( rm -r)

要删除（即删除）一个目录及其包含的所有子目录和文件，请导航到其父目录，然后使用命令rm -r后跟要删除的目录的名称（例如rm -r directory-name）。

例如，您可以删除assignments目录下的documents目录，因为它不符合目录好名的要求（即描述性不够——什么样的分配？）。

$ cd ~

$ cd documents

$ pwd

/users/jpalomino/documents

$ ls    

assignments  

$ rm -r assignments

rm代表删除，而有-r必要告诉Bash它需要通过父目录中所有文件和子目录的列表递归（或重复）命令。

这样，在删除时，新创建的homeworks目录assignments也将assignments被删除。

$ pwd

/users/jpalomino/documents

$ ls

## 7. 复制文件 ( cp)

您还可以使用命令将特定文件复制到新目录，cp后跟要复制的文件的名称以及要将文件复制到的目录的名称（例如cp filename directory-name）。

例如，您可以grades.txt从主目录复制到documents.

$ cd ~

$ pwd

/users/jpalomino

$ ls 

documents    downloads    grades.txt

$ cp grades.txt documents

$ cd documents

$ ls

grades.txt

请注意，文件的原始副本仍保留在原始目录中，因此您现在将拥有 的两个副本grades.txt，一个位于主目录中，另一个位于documents.

$ cd ~

$ pwd

/users/jpalomino

$ ls 

documents    downloads    grades.txt

## 8. 复制目录及其内容 ( cp -r)

同样，您可以将整个目录复制到另一个目录，使用cp -r后跟要复制的目录名称和要复制目录的目录名称（例如cp -r directory-name-1 directory-name-2）。

与 类似rm -r，-rincp -r有必要Bash通过父目录中所有文件和子目录的列表来告诉它需要递归（或重复）命令。

$ cd ~

$ pwd

/users/jpalomino

$ ls 

documents    downloads    grades.txt

$ mkdir pics

$ ls 

documents    downloads    grades.txt    pics

$ cp -r pics documents

$ cd documents

$ ls

grades.txt    pics

再次，目录的原始副本保留在原始目录中。

$ cd ~

$ pwd

/users/jpalomino

$ ls 

documents    downloads    grades.txt    pics

## 9.使用单个命令 ( touch)创建新文件


您可以使用单个命令touch（例如touch file-name.txt）创建一个新的空文件。此命令最初是为了管理文件的时间戳而创建的。但是，如果文件尚不存在，则该命令将生成该文件。

这是一种以编程方式快速创建新的空文件的非常有用的方法，该文件可以在以后填充。

$ cd ~

$ cd downloads

$ pwd

/users/jpalomino/downloads

$ touch veg-data.txt

$ ls

veg-data.txt

