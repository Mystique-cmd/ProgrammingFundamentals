#include <stdio.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <sys/utsname.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <string.h>

void File_Manipulator()
{
	// This function provides a simple file manipulation interface for the user.
// It allows the user to open a file in read, write, or create mode, and then
// either read from or write to the file based on user input.
// Parameters: None
// Return Value: None (void)
	char *poison = (char *)malloc(100 * sizeof(char)); // allocate memory for file name
	int how_open, file_descriptor, decision;
	char buffer[4096]; // its a temporary storage area to hold data while transfering  between processes,files or devices
	if (poison == NULL)
	{
		printf("Memory allocation failed\n");
		return;
	}

	// getting the file name from user
	printf("What file is your poison?\n");
	scanf("%99s", poison);

	// Select the file open mode
	printf("How do you want to open the file?\n1.Read Only\n2.Write Only\n3.Create New File\n");
	scanf("%d", &how_open);

	if (how_open == 1)
	{
		file_descriptor = open(poison, O_RDONLY);
	}
	else if (how_open == 2)
	{
		file_descriptor = open(poison, O_WRONLY);
	}
	else if (how_open == 3)
	{
		file_descriptor = open(poison, O_WRONLY | O_CREAT, 0644);
	}
	else
	{
		printf("Invalid Input\n");
		free(poison);
		return;
	}
	if (file_descriptor == -1)
	{
		perror("Error opening file");
		free(poison);
		return;
	}
	// Decide actions
	printf("What next?\n1.Read File\n2.Write Onto File\n");
	scanf("%d", &decision);

	if (decision == 1)
	{
		ssize_t bytes_read = read(file_descriptor, buffer, sizeof(buffer));
		//-1 : error in reading 0 : end of file
		if (bytes_read > 0)
		{
			if (bytes_read < sizeof(buffer))
				buffer[bytes_read] = '\0'; // Null terminate to prevent additional characters during printing
			else
				buffer[sizeof(buffer) - 1] = '\0'; // Ensure null-termination
			printf("File contents:\n%s\n", buffer);
		}
		else if (bytes_read == 0)
		{
			printf("File is empty.\n");
		}
		else
		{
			printf("Failed to read file\n");
		}
	}
	else if (decision == 2)
	{
		char data[4096]; // buffer for user input
		printf("Enter text to write on file:");
		getchar();						  // clears any leftover newline character in the input buffer
		fgets(data, sizeof(data), stdin); // get user input
		printf("Data written successfully!\n");
		if (strlen(data) > 1)
		{ // ensures the user actually typed something
			write(file_descriptor, data, strlen(data));
		}
		else
		{
			printf("No valid input provided\n");
		}
	}
	close(file_descriptor);
	free(poison);
}

void Executor()
{
	// This function prompts the user for the name of an executable file and attempts
// to execute it using execl(). It replaces the current process image with the new program.
// Parameters: None
// Return Value: None (void)
	char executable[256];

	// get the name of the executable
	printf("Your wish is my command...!What can I execute\n");
	scanf("%255s", executable);

	pid_t pid = fork();
	if (pid == -1) {
		perror("fork failed");
		return;
	} else if (pid == 0) {
		// Child process
	
	}
}
void Process_Management()
{
	// This function demonstrates basic process management by printing the current
// process ID and creating a child process using fork().
// Parameters: None
// Return Value: None (void)
	int Parent_Process = getpid();
	int child_process;
	// checking the PID of the current running process
	printf("Current Running Process : %d\n", getpid());

	// creating the child process
	// the fork  () doesnt take any arguments
	child_process = fork();
	// printf("The Child Process : %d\n",getpid());
}

void Terminal()
{
	// This function retrieves and displays the size of the terminal window (rows and columns)
// using the ioctl() system call.
// Parameters: None
// Return Value: None (void)
	// getting the terminal size
	// ioctl expects a pointer to a structure to store the terminal size information
	struct winsize w;
	ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);
	printf("Rows: %d, Columns: %d\n", w.ws_row, w.ws_col);
}

void System_Properties()
{
	// This function retrieves and displays system information such as system name,
// node name, release, version, and machine type using uname().
// Parameters: None
// Return Value: None (void)
	// getting the system properties
	struct utsname System_Information;
	if (uname(&System_Information) == 0)
	{
		printf("System: %s\n", System_Information.sysname);
		printf("Node Name: %s\n", System_Information.nodename);
		printf("Release: %s\n", System_Information.release);
		printf("Version : %s\n", System_Information.version);
		printf("Machine: %s\n", System_Information.machine);
	}
	else
	{
		perror("uname failed");
	}
}

int main()
{
	int Services;
	printf(" Hi there,welcome ..Here your wish is our command!\n");
	printf("Here is a list of our services:\n 1.File Manipulation\n2.Commands and Executables Executions\n3.Process Management\n4.Terminal Checks\n5.Checking System Properties\n");
	printf("What would you like to begin with?");
	scanf("%d", &Services);

	switch (Services)
	{
	case 1:
	{
		File_Manipulator();
		break;
	}
	case 2:
	{
		Executor();
		break;
	}
	case 3:
	{
		Process_Management();
		break;
	}
	case 4:
	{
		Terminal();
		break;
	}
	case 5:
	{
		System_Properties();
		break;
	}
	default:
	{
		printf("Wrong Choice Hun!\n");
		break;
	}
	}
	return 0;
}
