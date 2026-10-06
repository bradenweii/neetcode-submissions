class Solution {

    public String encode(List<String> strs) {
        String s ="";
        for(String str:strs){
            s+=str+"|";
        }
        return s;
    }

    public List<String> decode(String str) {
        List<String> arr= new ArrayList<>();
        String s="";
        for(int i=0;i<str.length();i++){
            
            if(str.charAt(i)=='|'){
                arr.add(s);
                s="";
            }else{
                s+=str.charAt(i);
            }
        }
        return arr;
    }
}
