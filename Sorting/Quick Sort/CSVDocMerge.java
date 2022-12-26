
Document Merge
Programming challenge description:
Write a program that will parse, combine, and output CSV documents. This will require you to work through the data and merge the data sets appropriately based on a unique "ID" identifier for each row.

For example:

ID,Name,Start,End
16,Abraham Lincoln,1861,1865
Merged with:

ID,Name,Start,End
15,James Buchanan,1857,1861
Would result in:

ID,Name,Start,End
15,James Buchanan,1857,1861
16,Abraham Lincoln,1861,1865
Input:
Two CSV-like documents split by an empty line. The first line of each "document" will be the header, with data following afterwards. Each value should always be treated as a string and will be separated by a comma as a control character. Each individual document should only contain unique IDs. The ID value should always be a string with a valid numeric value. The headers of both documents will be consistent. Each document will have at least one row in addition to the header. For example:

ID,Name,Start,End
16,Abraham Lincoln,1861,1865

ID,Name,Start,End
15,James Buchanan,1857,1861
Output:
A single CSV-like document as a result of the provided original documents. The first line should be the header with merged data on subsequent rows, sorted by the ID column. The output should only present one row per unique ID value. If a duplicate ID is provided, use the value in the second document in the results. For example:

ID,Name,Start,End
15,James Buchanan,1857,1861
16,Abraham Lincoln,1861,1865
Test 1
Test Input
Download Test 1 Input
ID,Name,Start,End
16,Abraham Lincoln,1861,1865

ID,Name,Start,End
15,James Buchanan,1857,1861
Expected Output
Download Test 1 Output
ID,Name,Start,End
15,James Buchanan,1857,1861
16,Abraham Lincoln,1861,1865
Test 2
Test Input
Download Test 2 Input
ID,First,Status,Title
541,Tim,Part Time,Accountant
327,Allison,Full Time,Information Security

ID,First,Status,Title
541,Tim,Full Time,Senior Accountant
100,Sally,Full Time,Line Manager
Expected Output
Download Test 2 Output
ID,First,Status,Title
100,Sally,Full Time,Line Manager
327,Allison,Full Time,Information Security
541,Tim,Full Time,Senior Accountant
Copyright 2012-2022 by HireVue. All rights reserved. Unauthorized copying, publication, or disclosure prohibited.
public class CSVDocMerge {

 * The Main class implements an application that reads lines from the standard input
 * and prints them to the standard output.
 */
public class Main {
  /**
   * Iterate through each line of input.
   */
  public static String docMerge(ArrayList<String> input)
  {
    if (input.size() == 0) return "";
    ArrayList<String[]> output = new ArrayList<String[]>();
    for ( String line: input)
    {
      if(line.charAt(0) == 'I') continue;
       String[] tokens = line.split(",");
      output.add(tokens);
    }
    int j =0;
    quickSort(output, 0, output.size()-1);
    for(int i=0; i<output.size()-1;i++)
    {
     String[] temp = output.get(i);
      if(temp[0].equals(output.get(i+1)[0]))
        output.remove(i);
    }
    
    StringBuilder outputStr = new StringBuilder();
    outputStr.append(input.get(0)+"\n");
    for( int i =0; i<output.size(); i++)
    {
      String[] line = output.get(i);
      outputStr.append(line[0]+","+line[1]+","+line[2]+","+line[3]+"\n");
    }
    return outputStr.toString();
  }
  static int partition(ArrayList<String[]> arr, int low, int high)
  {
    int pivot = Integer.parseInt((arr.get(high))[0]);
    int i = low -1;
    for(int j = low; j< high -1; j++)
    {
      String[] temp = arr.get(j);
      if(Integer.parseInt(temp[0]) < pivot)
      {
        i++;
        Collections.swap(arr, i , j);
      }
    }
    Collections.swap(arr, i+1, high);
    return (i+1);
  }
  static void quickSort(ArrayList<String[]> arr , int low, int high)
  {
    if (low<high)
    {
      int pi = partition(arr, low, high);
      quickSort(arr, low, pi-1);
      quickSort(arr, pi+1, high);
    }
  }
  public static void main(String[] args) throws IOException {
    InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
    BufferedReader in = new BufferedReader(reader);
    String line;
    ArrayList<String> input = new ArrayList<String>();
    while (true) {
     line = in.readLine();
      if(line == null) break; 
      if(line.trim().isEmpty()) continue;
      input.add(line);
    }
    System.out.println(docMerge(input));
  }
}

}
