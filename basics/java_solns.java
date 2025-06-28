import java.util.Scanner;

class Main
{
	public static void main(String[] args)
	{
	    Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		boolean evenNum = false;
		
		for (int i=0; i<n; i++){
		    arr[i] = sc.nextInt();
		}
		
		for (int i=0; i<n; i++){
		    if (arr[i] % 2 == 0){
		        System.out.print(arr[i] + " ");
		        evenNum = true;
		    }
		}
		
		if (!evenNum){
		    System.out.println("No Even Numbers.");
		}
		
		sc.close();
		
	}
}

import java.util.Scanner;

class Main
{
	public static void main(String[]args)
	{
		Scanner sc = new Scanner(System.in);
	    String input = sc.nextLine();
	    
	    int vowels = 0;
	    String consonants = "";
	    
	    if (!input.matches("[A-Za-z]+")){
	        System.out.print("Invalid Input");
	    }
	    else{
	        for (int i=0; i<input.length(); i++){
	            char ch = input.charAt(i);
	            char lc = Character.toLowerCase(ch);
	            
	            if (lc == 'a' || lc == 'e' || lc == 'i' || lc == 'o' || lc == 'u'){
	                vowels++;
	            }
	            else{
	                consonants += ch;
	            }
	        }
	        System.out.println("No of Vowels : " + vowels);
	        System.out.println("Consonants : " + consonants);
	        sc.close();
	    }
	}
}