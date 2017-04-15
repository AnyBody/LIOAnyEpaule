# LIOAnyEpaule

LIOAnyShoulder is an inverse dynamic musculoskeletal model of the shoulder
joint. Such analysis allows computation of muscular and joint reaction forces
based on a given motion. This study takes part of non-conforming total shoulder
arthroplasty. The prosthesis component implantation and position should require
two aspects:

* Integration, *.stl format, of total shoulder arthroplasty 3D model.
* Knowledge of matrix transformation between coordinate bone and implant systems.

Any methods could be perform to achieve these requirements. This tutorial will
describe the basics concepts to use AnybodyTM software and start working on the
musculoskeletal model of the shoulder joint.


## II. LIOAnyShoulder musculoskeletal model architecture and parameters
### 1. LIOAnyShoulder Model architecture

<p align="center">
  <img src="_static/repo.jpg"/>
  Necessary files for the proper functioning of the LIOAnyShoulder model are in bold
</p>

The AnyBody musculoskeletal model respects the hierarchical organization of
models present in the AnyBodyTM repository ([[#Section|'''Figure 3''': AnyBody
repository structure]]). The LIOAnyShoulder model files and the
LIOAnyEpaule.main.any are integrated in the Validation folder. The « STLModels »
folder in « Body » is intended to receive two model types:

* « ImplantModels » folder: 3D (*.stl) implant models 
* « Bones » folder: AnyBody bone, after scaling operations 

The following variables are used in this tutorial to make the reading easier: 
* [MainModelPath]:  folder which contains the LIOAnyShoulder model .Main.any file (Validation folder)
* [BodyPath] : dossier ‘Body’


## 2. Modifiable parameters of the LIOAnyShoulder 

There are two modifications that can be made in the LIOAnyShoulder: 

* <u> Model parameters</u>: Intrinsic parameters of musculoskeletal numerical
  model. Default values are the ones tested and validated. It is recommended to
  keep them as indicated, unless you would like to improve the model itself. Be
  careful, modifications to those parameters necessitate new steps of
  verification and validation for the model achieved.

* <u> Study parameters</u>: Modifiable parameters to study the muscular force
  effects and the contact of the glenoid component. Allows a sensitivity study
  to be performed to answer various clinical questions.

This part describes the functionality’s link with each parameter. It is organized like so: 

<u> Functionalities</u>: Description of the functionality strives by the parameter 
<u>Description</u>: Explanations and details about the utilisation of the functionality or about its integration <br>
<u>File</u>: Name of the file *.any in which the linked code is located <br>
<u>Path</u>: Path to the file <br>

Table columns are:

* <u>Definition</u>: Short parameter description <br>
* <u>Variable</u>: Variable name linked to the parameter <br>
* <u>Value</u>: Default parameter value and/or the value indicated in the RhodeCode code <br>
!! Warning !! For the parameter models, this value should be modifiable <br>
!! Warning !! For the parameter study, this value should be adapted for each study case. The default value is not, in any case, functional. <br>
* <u>Code</u>: Code / Function in the folder *.any



## III. Model parameters
### 1. 	Glenohumeral type joint

<u>Functionality</u>: Simulate (or not) humeral head and glenoid translations <br>
<u>Description</u>: Humeral head translations are part of the model, you should keep them.<br>
<u>File</u>: LoadValues.any <br>
<u>Path</u>: [MainModelPath]/Model <br>

<table>
    <tbody>
        <tr>
            <td>
                <p>Definition</p>
            </td>
            <td>
                <p>Variable</p>
            </td>
            <td >
                <p>Value</p>
            </td>
            <td>
                <p>Code</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><i>Option to activate or deactivate head-glenoid translation<p><i>
                <p>0: Articulation with 6 degrees of freedom (translations). Imply FDK utilisation [by default]</p>
                <p>1 : Ball&amp;Socket articulation (no translations)</p>
            </td>
            <td>
                <p>BallAndSocket</p>
            </td>
            <td >
                <p>0</p>
            </td>
            <td>
                <p>#define BallAndSocket 0</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><i>Algorithm FDK values (case 0, with translations)</i></p>
                <p>Non-liner model [Bigliani, 1992]:</p>
                <p>F : Force</p>
                <p>k&nbsp; : stiffness</p>
                <p>&alpha; : translation</p>
                <p>Medio-Lateral stiffness: manage by the contact between the stl. model.</p>
            </td>
            <td>
                <p>k<sub>0</sub></p>
                <p>k<sub>1</sub></p>
                <p>k<sub>2</sub></p>
                <p>k<sub>3</sub></p>
                <p>k<sub>4</sub></p>
                <p>k<sub>z</sub></p>
            </td>
            <td >
                <p>10,75</p>
                <p>-7787</p>
                <p>4391</p>
                <p>0</p>
                <p>&nbsp;- 0.08637</p>
                <p>0</p>
            </td>
            <td>
                <p>AnyFolder FDK ={<p>
                <p>&nbsp;AnyVar k0 = 10.75;&nbsp;&nbsp;</p>
                <p>&nbsp; AnyVar k1 = -7.787;&nbsp;</p>
                <p>&nbsp; AnyVar k2 = 4.391;</p>
                <p>&nbsp; AnyVar k3 = 0 ;</p>
                <p>&nbsp; AnyVar k4 = -0.08637 ;</p>
                <p>&nbsp; AnyVar kz = 0; };</p>
            </td>
        </tr>
    </tbody>
</table>


### 2. 	Contact with prosthetic components

<u>Functionality</u>: Contact consideration (or not) of the prosthetic components<br>
<u>Description</u>: 
* ''With contact'': Reaction force calculation when a linear reaction exists between the penetration and the stiffness impact. This case leads to the following estimated parameters: pressure, pressure center position and movement, contact surface. 
* ''Without contact'': GH reaction force calculation as the virtual muscles sum forcing the path of this force into the glenoid.  This latest is roughly represented by a sphere. The ‘without contact’ condition corresponds to the « BergmannGH » model in the repository AnyBody.
<u>File</u>: LoadValues.any <br>
<u>Path</u>: [MainModelPath]/Model

{| class="wikitable alternance center"

{|  border="1" style="border: 1px solid black  width="50%" ;"
 |----
 ! Definition !! scope="col" |Variable !! scope="col" |Value !! scope="col"|Code
 |----
 |  |''Option to activate or deactivate head-glenoid translation'' <br>0 : No head - glenoid contact (i.e. no contact calculation + GH-JRF = sum of applied around the glenoid)<br> 1 : Head – glenoid contact [by default]|| align="center" |stl|| align="center" |0|| #define stl 1 
 |----
|  |Stiffness for contact algorithn|| align="center" |k<sub>d<sub>|| align="center" |0||AnyFolder Contact ={<br>AnyVar kd =1e10;};
 |----

|}

###  3. Muscular visualisation
<u>Functionality</u>: Option to visualize (developing option)<br>
<u>Description</u>: This option allows you to show or to hide the nodes in the muscular model. It only affects the visual representation and has no influence on the calculations.<br>
<u>File</u>: LoadValues.any <br>
<u>Path</u>: [MainModelPath]/Model<br>


{| class="wikitable alternance center"

{|  border="1" style="border: 1px solid black  width="50%" ;"
 |----
 ! Definition !! scope="col" |Variable !! scope="col" |Value !! scope="col"|Code
 |----
 |  |Show/hide (0/1) insertion muscular points|| align="center" |ShowNodes|| align="center" |0|| #define ShowNodes 0 
 |----
|  |Show/hide (0/1) bones during the scaling process based on the CT-Scan reconstructions <br> based on the reconstructions CT-Scan.|| align="center" |dev|| align="center" |0||#define dev 0
 |----

|}

## IV. Study parameters

###  1. Prosthetic component placement

<u>Functionality</u>: Implantation and position of prosthetic components in the musculoskeletal model.<br>
<u>Description</u>: Integration of prosthetic components in the musculoskeletal model is done with the 3D model *.stl  format. They are automatically converted by AnyBody in the *.anysurf3 format. The component placement within bones is done thanks to a transformation matrix from AnyBody bone coordinates toward the implant coordinates. <br>
<u>File</u>: InputVariables.any <br>
<u>Path</u>: [MainModelPath]/Model <br>

{| class="wikitable alternance center"

{|  border="1" style="border: 1px solid black  width="50%" ;"
 |----
 ! Definition !! scope="col" |Variable !! scope="col" |Value !! scope="col"|Code
 |----
 |  |Name of the file which contains the implant information|| align="center" |INPUTPOS|| align="center" |ImplantName|| #define INPUTPOS "ImplantName" 
 |----
|}

### 2. Different muscular conditions simulation 

<u>Functionality</u>: different shoulder muscular conditions, pathological or not <br>
<u>Description</u>: The default case is the non-pathological shoulder. Different rotator cuff muscle ruptures can be studied, like the examples below.  <br>
<u>File</u>: InputVariables.any  <br>
<u>Path</u>: [MainModelPath]/Model <br>

{| class="wikitable alternance center"

{|  border="1" style="border: 1px solid black  width="50%" ;"
 |----
 ! Definition !! scope="col" |Variable !! scope="col" |Value !! scope="col"|Code
 |----
 |  |0 : No rupture [by default]<br>1 : Supraspinatus rupture<br>2 : supraspinatus + infraspinatus rupture<br>3 : Massive rupture: supraspinatus + infraspinatus + <br> 2/3 superior of  subscapular [1]<br>4 : Subscapular rupture (total) [2]<br>5 : 2/3 Superior of subscapular || align="center" |Tear|| align="center" |0|| #define Tear 0 
 |----
|}

### 3. Save the results

<u>Functionality</u>: Save automatically or manually analyse results. <br>
<u>Description</u>: Output formats are text or anydata.h5. <br>
<u>File</u>: InputVariables.any <br>
<u>Path</u>: [MainModelPath]/Model<br>

{| class="wikitable alternance center"

{|  border="1" style="border: 1px solid black  width="50%" ;"
 |----
 ! Definition <br> ''Name and localisation of the results file '' !! scope="col" |Variable !! scope="col" |Value !! scope="col"|Code
 |----
|  |Name of the results file|| align="center" |m_ResultFile|| align="center" |ResultFileName||#define NameFile "ResultFileName"
 |---- 
|  |Folder of the results files (do not forget to create one in the computer first)|| align="center" |m_ResultFolder|| align="center" |Results||#define NameFolder "Results\"
 |----
|  |Path toward the results folder || align="center" |m_ResultPath|| align="center" |D:\Docs\CompletPathToResults||#define NamePath "D:\Docs\Complet\Path\To\Results\"
 |----
|}

<u>File</u>: RunAppSequence.any <br>
<u>Path</u>: [BodyPath]/AAUHuman/Toolbox/Operations

{| class="wikitable alternance center"

{|  border="1" style="border: 1px solid black  width="50%" ;"
 |----
 ! Definition !! scope="col" |Variable !! scope="col" |Value !! scope="col"|Code
 |----
 |  |[anydata*.h5] Macro to save all the data in a hierarchical type file  (= tree which contain all data’s model)|| align="center" |Macro SaveDataDeep || align="center" |''{None :no macro to launch}''||[[Image:code3.png]]
 |----
|}

<u>File</u>: LoadValues.any<br>
<u>Path</u>:[MainModelPath]/Model

{| class="wikitable alternance center"

{|  border="1" style="border: 1px solid black  width="50%" ;"
 |----
 ! Definition !! scope="col" |Variable !! scope="col" |Value !! scope="col"|Code
 |----
 |  |[*.txt] Choice of parameters to integrate || align="center" |ActivityOutput,<br> ForcesOutput,<br> MomentOutput, <br>PowerOutput, <br>LeverArmOutput, <br>StrengthOutput,<br> LmtOutput,<br> DeltoidOutput,<br> CuffOutput        || align="center" |1|| [[Image:code.png]]
 |----
|}

<u>File</u>: Output_CheckName.any, filename.py, filename.pyc <br>
<u>Path</u>: [MainModelPath]/Output

{| class="wikitable alternance center"

{|  border="1" style="border: 1px solid black  width="50%" ;"
 |----
 ! Definition !! scope="col" |Variable !! scope="col" |Value !! scope="col"|Code
 |----
 |  |[*.txt] Verification of existing file or not, to not lose the old one. If existing file, make the name sequential file.  || align="center" |N/A|| align="center" |''{None : Python fonctions}''|| [[Image:code2.png]] 
|----
|}

File: Output_File.any, Output_Deltoid.any, Output_Cuff.any <br>
Path: [MainModelPath]/ Output

{| class="wikitable alternance center"

{| border="1" style="border: 1px solid black  width="50%" ;"
 |----
 ! Definition !! scope="col" |Variable !! scope="col" |Value !! scope="col"|Code
 |----
 |  |[*.txt] Write the results in a .txt  file. || align="center" |N/A|| align="center" |N/A|| N/A
|----
|}

=V. LIOAnySoulder Model: two classical analyses step by step= 
== 1. Background ==

This section presents steps to follow in order to help you beginning the AnyBody software using the LIOAnyShoulder model. <br>
''Warning'': This section treats only the case where the model is used in the total anatomic prosthesis context. That means, the following parameters are selected and cannot be modified in this presentation: 

* Glenohumeral joint	: BallAndSocket == 0
* Contact between implants	: stl == 1 
Refer to [[#section| 2. Modifiable parameters of the LIOAnyShoulder]] chapter to know the different options available for each variable used in this step by step guide. Inputs assigned to variables are referenced [bracketed text].

It is considered that: 

* The 1.0Beta version of LIOAnyShoulder has been downloaded 
* The folder contains the whole model located in the accessible writing disk. Avoid the C:/ if you do not have administrator rights.

== 2. Analyse with the generic model ==

Follow the instructions:

{| class="wikitable alternance center"

{|  border="1" style="border: 1px solid black  width="70%" ;"
 |----
 ! Step !! scope="col" | Description !! scope="col"| Reference <br> ''(method, variable, Figure)''
 |----
 | align="center" | 1 || '''Start the software AnyBody 6.0'''
 |----
 | align="center" | 2 || '''Open the folder LioAnyShoulder.main.any''' <br> File > Open… (or folder icon, menu bar). The folder *.main.any is in the folder LIOAnyÉpaule, under Validation. || align="center" | [[Figure 3: AnyBody repository structure.]]
 |----
 | align="center" | 3 || '''Open the folder InputVariables.any''' <br> Two possibilities : <br> o Double click on the line: #include "Input/InputVariables.any"<br>o File > Open > Input > InputVariables.any || align="center"| [[Menu]]
 |----
 | align="center" | 4|| '''Name of file and folder'''  <br> o [m_ResultFile]: Name for results file you need to create <br> o [m_ResultFolder] : Name for folder where the result file is saved <br> o [m_ResultPath]: Path to m_ResultFolder <br> WARNING : <br> o Variables m_ResultFolder and m_ResultPath need to finish by a slash (/) <br> o	Folder m_ResultFolder: needs to exist. If it is not the case, create it when you start the analysis. || align="center"| [[Save the results]]
 |----
 | align="center" | 5 || '''Implants''' <br> '''3D implant models files''' <br>o Make sure the 3D models of prosthesis components (prosthetic humoral head and glenoid implant) *.stl format are in the folder: [BodyPath]\STLModels\ImplantModels <br> o If this is not the case, put them in.<br>'''Modify InputVariables.any file'''<br> o [INPUTPOS] : Give a significant name for the implants used (ex : CeraverT351 : implants Ceraver, glenoid size 3, head diameter 51) <br> '''Create InputImplantJoint_[INPUTPOS].any file'''<br> o Duplicate template file [MainModelPath]/Input./InputImplantJoint_ImplantName.any <br> o Assign it a name : InputImplantJoint_[INPUTPOS].any <br> o	Open the file you just created   || align="center"| [[LIOAnyShoulder musculoskeletal model architecture and parameters]] <br><br> [[Prosthetic components placement]] <br> <br>[[Prosthetic components placement]]
 |----
|}

 |}
