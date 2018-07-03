function th = running_average(pix_vec, s, current_avg, count)

% pix_vec = double(pix_vec);
% 
% th = 0;
% 
% for i = 0 : size(pix_vec,1)-1
%    
%     th  = th + ((1- 1/s)^(i))*pix_vec(end-i,1);
%     
% end
% 
% th = th + current_avg*((1-1/s)^(size(pix_vec,1)));

if(count < s)
    th = (current_avg*count + pix_vec)/(count+1);
else
    th = current_avg*s - current_avg + pix_vec(end,1);
    th = th/s;
end



end
