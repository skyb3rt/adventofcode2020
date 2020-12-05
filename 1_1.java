import java.util.*;
import java.util.ArrayList;
import java.io.File;


class AdvendtOfCode {

    public static void main(String[] args) throws Exception{
        System.out.println(finn_to(2020,read_file()));
        
    }
        
    public static ArrayList<Integer> read_file() throws Exception{
        ArrayList<Integer> l = new ArrayList<Integer>();
        File myObj = new File("1.txt");
        Scanner myReader = new Scanner(myObj);
        while (myReader.hasNextLine()) {
            int data = Integer.valueOf(myReader.nextLine());
            l.add(data);        
        }
        myReader.close();
        return l;
    }

    public static Integer finn_to(Integer verdi, ArrayList<Integer> l){
        for (int i : l){
            int num= verdi-i;
            if (l.contains(num)){
                return(num* i); 
            }
        }
        return 0;
    }
}
