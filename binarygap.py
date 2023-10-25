def Solution(N):
    binary = str(format(N,'b'))
    count=0
    ll = []
    for i in range(len(binary)):
        if(binary[i]=='1') and ((i+1) < len(binary)) and (binary[i+1]=='0' ):
            count +=1
            i+=1
            while (len(binary) > (i+1)) and (binary[i+1] == '0' ):
                count+=1
                i+=1
                if((i+1) < len(binary)) and (binary[i+1]=='1'):
                    break

            if (len(binary) > (i+1)) and (binary[i+1]=='1'):
                ll.append(count)
                count =0

    if len(ll)==0:
        return 0
    else:
        return max(ll)