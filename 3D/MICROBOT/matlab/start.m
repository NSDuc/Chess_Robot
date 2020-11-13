if ~isempty(instrfind)
   fclose(instrfind);
   delete(instrfind);
end
s = serial('COM4','BaudRate',9600,'DataBits', 8,'Terminator',13);
s.ReadAsyncMode = 'continuous';
fopen(s);
set_param('MICROBOT_1/step1', 'Value', num2str(0));
set_param('MICROBOT_1/step2', 'Value', num2str(0));
set_param('MICROBOT_1/step3', 'Value', num2str(0));
set_param('MICROBOT_1/step4', 'Value', num2str(0));
set_param('MICROBOT_1/step5', 'Value', num2str(0));
set_param('MICROBOT_1/step6', 'Value', num2str(0));
while 1
    if s.BytesAvailable > 0
        out = fscanf(s)
        l = length(out);
        if l > 0
            header = out(1:5);
            if strcmpi(header, '@STEP')
               step = strsplit(out(7:(l - 4)), ', ');
               
               step_num = cellfun(@str2num,step)
               
               if step_num(3) ~= 0
                   step_num(4) = step_num(3) * -0.588
               end
               
               if step_num(4) ~= 0 && step_num(4) == step_num(7)
                    step_num(7) = 0
                    step_num(5) = step_num(4) * -0.369
               end
               
               if step_num(6) ~= 0 && step_num(6) == -step_num(5)
                   step_num(5) = 0
               end
               
       
               step_num
               set_param('MICROBOT_1/step1', 'Value', num2str(step_num(2)));
               set_param('MICROBOT_1/step2', 'Value', num2str(step_num(3)));
               set_param('MICROBOT_1/step3', 'Value', num2str(step_num(4)));
               set_param('MICROBOT_1/step4', 'Value', num2str(step_num(5)));
               set_param('MICROBOT_1/step5', 'Value', num2str(step_num(6)));
               set_param('MICROBOT_1/step6', 'Value', num2str(step_num(7)));
               set_param('MICROBOT_1/delay', 'Value', num2str(step_num(8)));
               set_param('MICROBOT_1/id', 'Value', num2str(step_num(9)));
            end
        end
    end
    pause(0.1);
end