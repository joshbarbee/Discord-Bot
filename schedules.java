import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Node;
import org.w3c.dom.Element;
import java.io.File;

public class blaaaa {

  public static void main(String argv[]) {

    try {

	File fXmlFile = new File("/Users/Su/Documents/calendar.xml");
	DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
	DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
	Document doc = dBuilder.parse(fXmlFile);

	//optional, but recommended
	//read this - http://stackoverflow.com/questions/13786607/normalization-in-dom-parsing-with-java-how-does-it-work
	doc.getDocumentElement().normalize();

	System.out.println("Root element :" + doc.getDocumentElement().getNodeName());

	NodeList nList = doc.getElementsByTagName("vevent");

	System.out.println("----------------------------");

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
			String daka = eElement.getElementsByTagName("description").item(0).getTextContent();

			String str = daka.replace("<p>", " ");
			str = str.replace("<br>", "\n");
			str = str.replaceAll("</p>", "");
			
			
			System.out.println("Current Schedule: " + eElement.getElementsByTagName("summary").item(0).getTextContent());
			System.out.println("Date : " + eElement.getElementsByTagName("dtstart").item(0).getTextContent());
			System.out.println(str) ;
			/*System.out.println("Salary : " + eElement.getElementsByTagName("salary").item(0).getTextContent());*/
		}
	}
    }
		
	
    
    catch (Exception e) {
	e.printStackTrace();
    }
  }
  }
