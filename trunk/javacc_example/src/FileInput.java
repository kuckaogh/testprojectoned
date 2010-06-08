import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;


public class FileInput {
 
	private File dataFile = new File("h.txt");
	public String sCurrentLine;
    public BufferedReader br;
    
	public void loaddata(){
	try{	

            br = new BufferedReader(new FileReader(dataFile));
		
        while ((sCurrentLine = br.readLine()) != null) {
 	       System.out.println(sCurrentLine);
 	    } 
		
		}
    	catch (FileNotFoundException e) { 
        e.printStackTrace();
    	} 
    	catch (IOException e) {
   
        e.printStackTrace();
   
      }
	}
  

	public static void main(String[] args) throws ParseException{
 
     FileInput test = new FileInput();
	 test.loaddata();
	 Calculator parser;

		try {
			parser = new Calculator(new FileInputStream("h.txt"));
			
	        while (true)
	        {
	            parser.parseOneLine();
	        }
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}


  }

 }