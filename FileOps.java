import java.io.*;

public class FileOps {
    public static void main(String[] args) {
        try {
            FileWriter writer = new FileWriter("example.txt");
            writer.write("Hello, File System in Java!\n");
            writer.close();
            BufferedReader reader = new BufferedReader(new FileReader("example.txt"));
            System.out.println("File content: " + reader.readLine());
            reader.close();
        } catch (IOException e) {
            System.out.println("Error occurred");
        }
    }
}
