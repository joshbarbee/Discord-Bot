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

	//File fXmlFile = new File("/Users/Su/Documents/xmldates/201711"+currentday+".xml");
	File fXmlFile = new File("/Users/Su/Documents/calendar.xml");
	DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
	DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
	Document doc = dBuilder.parse(fXmlFile);

	//optional, but recommended
	//read this - http://stackoverflow.com/questions/13786607/normalization-in-dom-parsing-with-java-how-does-it-work
	doc.getDocumentElement().normalize();

	//System.out.println("Root element :" + doc.getDocumentElement().getNodeName());

	NodeList nList = doc.getElementsByTagName("vevent");

	//System.out.println("----------------------------");

	for (int temp = 0; temp < 1; temp++) {   //nList.getLength()
		
		Node nNode = nList.item(temp);
		
		//System.out.println("\nCurrent Element :" + nNode.getNodeName());
		
		if (nNode.getNodeType() == Node.ELEMENT_NODE) {

			Element eElement = (Element) nNode;
			
			if (eElement == null || eElement.getElementsByTagName("description").item(0) == null)
			{
				System.out.println("Probably casting is no good");
				continue;
			}
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
			String daka = eElement.getElementsByTagName("description").item(0).getTextContent()+ " ";
			String Daytype = eElement.getElementsByTagName("summary").item(0).getTextContent();
			
			String newdate = month + " "+ date.substring(6, 8) + " " +date.substring(0, 4);
			String schedule = daka.replaceAll("<br>", "\n").replaceAll("<p>", "").replaceAll("</p>", " ");
			if (Daytype.contains("Assembly"))
			{
				String firstbell = schedule.substring(0, 11);
				String secondbell = schedule.substring(12, 23);
				String thirdbell = schedule.substring(24, 36);
				String fourthbell = schedule.substring(37,57);
				String fifthbell = schedule.substring(57, 74);
				String sixthbell = schedule.substring(74, 86);
				String seventhbell = schedule.substring(87, 100);
				String eigthbell = schedule.substring(100, 113);
				String ninthbell = schedule.substring(113, 126);
				
			
				System.out.println("Current Schedule: " + Daytype);
				System.out.println("Date : "+ newdate);
				System.out.println(schedule);
				

			}
			else if (Daytype.contains("All"))
			{
				String firstbell = schedule.substring(0, 11);
				String secondbell = schedule.substring(12, 23);
				String thirdbell = schedule.substring(24, 36);
				String fourthbell = schedule.substring(37,57);
				String fifthbell = schedule.substring(57, 74);
				String sixthbell = schedule.substring(74, 86);
				String seventhbell = schedule.substring(87, 100);
				String eigthbell = schedule.substring(100, 113);
				String ninthbell = schedule.substring(113, 126);
				
			
				System.out.println("Current Schedule: " + Daytype);
				System.out.println("Date : "+ newdate);
				System.out.println(schedule);
			}
			else
			{
				String firstbell = schedule.substring(0, 11);
				String secondbell = schedule.substring(12, 23);
				String thirdbell = schedule.substring(24, 36);
				String fourthbell = schedule.substring(37,57);
				String fifthbell = schedule.substring(57, 74);
				String sixthbell = schedule.substring(74, 86);
				String seventhbell = schedule.substring(87, 100);
				String eigthbell = schedule.substring(100, 113);
				String ninthbell = schedule.substring(113, 126);
				
			
				System.out.println("Current Schedule: " + Daytype);
				System.out.println("Date : "+ newdate);
				System.out.println(schedule);
			}
			
			
			
			
			
		}
	}
    }
	catch (Exception e) {
    System.out.println(killme);
    System.out.println("\n\n\nNo classes to display\n\n\n");
	
	}
    }
}
    
		

  

}
