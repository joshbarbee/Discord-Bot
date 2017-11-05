import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Node;
import org.w3c.dom.Element;
import java.io.File;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.*;



public class blaaaa {

  public static void main(String argv[]) {
	 DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd");
	 Date currentdate = new Date();
	 String killme = dateFormat.format(currentdate); 
	 String currentday = killme.substring(8,10);
	 

    try {

	File fXmlFile = new File("/Users/Su/Documents/xmldates/201711"+currentday+".xml");
	DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
	DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
	Document doc = dBuilder.parse(fXmlFile);

	//optional, but recommended
	//read this - http://stackoverflow.com/questions/13786607/normalization-in-dom-parsing-with-java-how-does-it-work
	doc.getDocumentElement().normalize();

	//System.out.println("Root element :" + doc.getDocumentElement().getNodeName());

	NodeList nList = doc.getElementsByTagName("vevent");

	//System.out.println("----------------------------");

	for (int temp = 0; temp < nList.getLength(); temp++) {

		Node nNode = nList.item(temp);
		
		//System.out.println("\nCurrent Element :" + nNode.getNodeName());
		
		if (nNode.getNodeType() == Node.ELEMENT_NODE) {

			Element eElement = (Element) nNode;
			
			if (eElement == null || eElement.getElementsByTagName("description").item(0) == null)
			{
				System.out.println("Probably casting is no good");
				continue;
			}
			String daka = eElement.getElementsByTagName("description").item(0).getTextContent()+ " ";
			String date = eElement.getElementsByTagName("dtstart").item(0).getTextContent();
	        String month = date.substring(4,6);
	        
	        String Gregory = date.substring(0, 4)+ "/"+month+"/"+date.substring(0,4);
	        
			if (killme == Gregory)
			{
				continue;
			}
			else
			
				fXmlFile = new File("/Users/Su/Documents/xmldates/" + currentday + ".xml");
				
			switch (month)
	        {
		        case "1":  month = "January";
	            	break;
		        case "2":  month = "February";
	            	break;
		        case "3":  month = "March";
	            	break;
		        case "4":  month = "April";
	            	break;
		        case "5":  month= "May";
	            	break;
		        case "6":  month = "June";
	            	break;
		        case "7":  month = "July";
	            	break;
		        case "8":  month = "August";
	            	break;
		        case "9":  month = "September";
	            	break;
		        case "10": month = "October";
	            	break;
		        case "11": month = "November";
	            	break;
		        case "12": month = "December";
	            	break;
		        default: month = "Invalid month";
	            	break;
	        }
	        String newdate = month + " "+ currentday + " " +date.substring(0, 4);
			String schedule = daka.replaceAll("<br>", "\n").replaceAll("<p>", "").replaceAll("</p>", " ");
	
			System.out.println("Current Schedule: " + eElement.getElementsByTagName("summary").item(0).getTextContent());
			System.out.println("Date : "+ newdate);
			System.out.println(schedule);
	        
			}
	}
    }
		catch (Exception e) {
    	System.out.println(killme);
    	System.out.println("\n\n\nNo classes to display\n\n\n");
	
    }
  }
}
  
