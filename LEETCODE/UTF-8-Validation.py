class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        remaining_byte = 0

        for i in data:
            
            if remaining_byte == 0:
                
                if (i >> 5) == 0b110:
                    remaining_byte = 1
                    
                elif (i >> 4) == 0b1110:
                    remaining_byte = 2
                
                elif (i >> 3) == 0b11110:
                    remaining_byte = 3

                elif (i >> 7) != 0b0:
                    return False
   
            else:

                if (i >> 6) != 0b10:
                    return False
                else:
                    remaining_byte = remaining_byte - 1

        if remaining_byte == 0:
            
            return True
        
        else:
            return False   