function varargout = user_interface(varargin)
% USER_INTERFACE MATLAB code for user_interface.fig
%      USER_INTERFACE, by itself, creates a new USER_INTERFACE or raises
%                                                
%      singleton*.
%
%      H = USER_INTERFACE returns the handle to a new USER_INTERFACE or the handle to
%      the existing singleton*.
%
%      USER_INTERFACE('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in USER_INTERFACE.M with the given input arguments.
%
%      USER_INTERFACE('Property','Value',...) creates a new USER_INTERFACE or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before user_interface_OpeningFcn gets called.  An
%      unrecognized pro                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            perty name or invalid value makes property application
%      stop.  All inputs are passed to user_interface_OpeningFcn clsvia varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help user_interface

% Last Modified by GUIDE v2.5 07-May-2020 20:21:42

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
    'gui_Singleton',  gui_Singleton, ...
    'gui_OpeningFcn', @user_interface_OpeningFcn, ...
    'gui_OutputFcn',  @user_interface_OutputFcn, ...
    'gui_LayoutFcn',  [] , ...
    'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before user_interface is made visible.
function user_interface_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to user_interface (see VARARGIN)

% Choose default command line output for user_interface
handles.output = hObject;
global currentj1;
global currentj36;
global currentj6;
currentj1 = 0;
currentj36 = 0;
currentj6 = 0;
global frame1
global frame2
% Update handles structure
guidata(hObject, handles);

% UIWAIT makes user_interface wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = user_interface_OutputFcn(hObject, eventdata, handles)
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, ~, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global frame1
load camera;
set(hObject, 'String','processing');
handles.cam1 = webcam(1);
handles.cam1.Resolution = '1280x960';
frame1 = snapshot(handles.cam1);
frame1 = undistortImage(frame1,cameraParams);
%frame1 = imadjust(frame1,[],[],1);
delete(handles.cam1);
axes(handles.axes1);
imshow(frame1);
clear cam1;
[c, selc, posX, posY, openbw, src] = catchroi(frame1);
%assignin('base','selc',selc);
%assignin('base','posX',posX);
%assignin('base','posY',posY);
regionXb = c(selc,1);
regionXe = c(selc,1) + c(selc,3);
regionYb = c(selc,2);
regionYe = c(selc,2) + c(selc,4);

for i=1:size(selc)
    eval(['roi',num2str(i),'= src(regionYb(',num2str(i),'):regionYe(',num2str(i),...
        '),regionXb(',num2str(i),'):regionXe(',num2str(i),'),:);'])
    eval(['assignin(''base'',''roi',num2str(i),''',roi',num2str(i),');'])
end
axes(handles.axes3);
imshow(openbw);
%---------------
axes(handles.axes5);
imshow(roi4);
%-------------
for i=1:size(selc)
    eval(['roi = im2uint8(roi',num2str(i),');'])
    assignin('base','roi',roi);
    predictedLabel(i) = ConvoNN(roi);
end
assignin('base','predictedLabel',predictedLabel);

predicted = string(predictedLabel);
%assignin('base','predicted',predicted);
chessdata = [predicted', posX, posY];
posi = [posX, posY];  
assignin('base','posi',posi);
[m,n] = size(chessdata);
Z = arrayfun(@(x)char(chessdata(x)),1:numel(chessdata),'uni',false);
z = reshape(Z,m,3);
%assignin('base','z',z);
set(handles.uitable1,'data',z);
[chess,order,index,prior] = calcu_position(predicted,posX,posY);
handles.selc = selc;
handles.chess = chess;
handles.order = order;
handles.index = index;
handles.prior = prior;
%assignin('base','chess',chess);
assignin('base','prior',prior);
%assignin('base','index',index);
handles.predicted = predicted;
guidata(hObject,handles)
set(hObject, 'String','recognition');
%}

% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if strcmp(get(hObject,'String'),'connect')
    s = serial('COM1','BaudRate',9600,'DataBits', 8,'Terminator','CR');
    try
        fopen(s);
        handles.s = s;
        set(hObject, 'String','disconnect');
    catch e
        errordlg(e.message);
    end
    
else
    fclose(handles.s);
    set(hObject, 'String','connect');
end
guidata(hObject, handles);


% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

if strcmp(get(hObject,'String'),'stop')
    set(hObject, 'String', 'continue');
    % pause it:
    waitforbuttonpress;
else
    % otherwise, "resume" it:
    set(hObject, 'String', 'stop');1
end;
%return;

% --- Executes on button press in pushbutton5.
function pushbutton5_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

button = questdlg('Close','Warning','Not OK','OK','OK');
if strcmp(button,'OK')
    if isfield(handles,'s')
        fclose(handles.s);
    end
    close(gcf);
else
    return;
end


% --- Executes on button press in pushbutton6.
function pushbutton6_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
set(hObject, 'String','processing');

global currentj1; global currentj36;
load chesslocation.mat

selc = handles.selc;
chess = handles.chess;
order = handles.order;
index = handles.index;
prior = handles.prior;
predicted = handles.predicted;
L = size(selc,1);
s = handles.s;
[~,sortidx] = sortrows(order,1);
assignin('base','sortidx',sortidx);
sortchess = index(sortidx,:);
assignin('base','sortchess',sortchess);
for j = 1:L
    curt_tag = sortchess(j,find(sortchess(j,:)));
    tag_check = find(strcmp(prior(curt_tag,9),"0"));
    tag = curt_tag(tag_check(1));
    %assignin('base','curt_tag',curt_tag);
    %assignin('base','tag_check',tag_check);
    %assignin('base','tag',tag);
    %chesslocation(tag,9) = "1";
    %assignin('base','chesslocation',chesslocation);
    %[currentj1,currentj36] =robot_clamp(s,chess(sortidx(j),1),chess(sortidx(j),2),chess(sortidx(j),3),chess(sortidx(j),5),currentj1,currentj36);
    [currentj1,currentj36] =robot_clamp2(s,chess(sortidx(j),1),chess(sortidx(j),2),chess(sortidx(j),3),chess(sortidx(j),5),currentj1,currentj36);
    %assignin('base','currentj1',currentj1);
    %assignin('base','currentj36',currentj36);
    
    if tag == 23
        %[currentj1,currentj36] =robot_turn(s,currentj1,currentj36);
        [currentj1,currentj36] =robot_turn_2(s,currentj1,currentj36);
        global frame2
        load camera;
        handles.cam1 = webcam(1);
        handles.cam1.Resolution = '1280x960';
        frame2 = snapshot(handles.cam1);
        frame2 = undistortImage(frame2,cameraParams);
        delete(handles.cam1);
        clear cam1;
        %axes(handles.axes5);
        %imshow(frame2);
        [tx, ty] = turn_catch(frame2);
        turnroi = frame2(tx-50:tx+49,ty-50:ty+49,:);
        %axes(handles.axes7);
        %imshow(turnroi);
        roi = im2uint8(turnroi);
        predictedLabel(L+1) = ConvoNN(roi);
        predicted(L+1) = string(predictedLabel(L+1));
        assignin('base','predicted',predicted);
        pause(0.1)
        %if exist(predicted(L+1)) ~= 0
            curt_tag = find(strcmp(predicted(L+1),prior));
            tag_check = find(strcmp(prior(curt_tag,9),"0"));
            tag = curt_tag(tag_check(1));
            %[currentj1,currentj36] =robot_turn2(s,currentj1,currentj36);
            [currentj1,currentj36] =robot_turn2_2(s,currentj1,currentj36);
            robo_tag(j,:) = str2double(prior(tag,4:8));
        %end
    else
        robo_tag(j,:) = str2double(prior(tag,4:8));
    end
    %[currentj1,currentj36,check] =robot_place(s,robo_tag(j,1),robo_tag(j,2),robo_tag(j,3),...
    %    robo_tag(j,4),robo_tag(j,5),currentj1,currentj36);
    [currentj1,currentj36,check] =robot_place2(s,robo_tag(j,1),robo_tag(j,2),robo_tag(j,3),...
        robo_tag(j,4),robo_tag(j,5),currentj1,currentj36);
    prior(tag,9) = check;
    assignin('base','chesslocation',chesslocation);
    %}
end
%[currentj1,currentj36] =robot_reset(s,currentj1,currentj36);
axes(handles.axes5);
imshow(frame2);

set(hObject, 'String','start');


% --- Executes on button press in pushbutton7.
function pushbutton7_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global currentj6;
if strcmp(get(hObject,'String'),'robot_on')
    gp_on = ['@STEP 221,0,0,0,0,0,430,0'];fprintf(handles.s,gp_on);
    currentj6 = 430;
    set(hObject, 'String', 'robot_off');
else
    gp_off = ['@STEP 221,0,0,0,0,0,-430,0'];fprintf(handles.s,gp_off);
    currentj6 = 0;
    set(hObject, 'String', 'robot_on');
end


% --- Executes when entered data in editable cell(s) in uitable1.
function uitable1_CellEditCallback(hObject, eventdata, handles)
% hObject    handle to uitable1 (see GCBO)
% eventdata  structure with the following fields (see MATLAB.UI.CONTROL.TABLE)
%	Indices: row and column indices of the cell(s) edited
%	PreviousData: previous data for the cell(s) edited
%	EditData: string(s) entered by the user
%	NewData: EditData or its converted form set on the Data property. Empty if Data was not changed
%	Error: error string when failed to convert EditData to appropriate value for Data
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function uitable1_ButtonDownFcn(hObject, eventdata, handles)
% hObject    handle to uitable1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes when selected cell(s) is changed in uitable1.
function uitable1_CellSelectionCallback(hObject, eventdata, handles)
% hObject    handle to uitable1 (see GCBO)
% eventdata  structure with the following fields (see MATLAB.UI.CONTROL.TABLE)
%	Indices: row and column indices of the cell(s) currently selecteds
% handles    structure with handles and user data (see GUIDATA)
