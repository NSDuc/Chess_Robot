/* SimMechanics target specific file
 *      This file generated a part of SimMechanics code generation.
 */
#include "rtwtypes.h"
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "mech_std.h"
#include "mtypes.h"
#include "simulation_data.h"
#include "sim_mechanics_imports.h"
#include "rt_mechanism_data.h"
/*
 * Convert runtime parameter vector for machine to structure
 */
void rt_vector_to_machine_parameters_MICROBOT_1_e2dc272(const real_T *_mech_rtP, MachineParameters_MICROBOT_1_e2dc272 *_mech_rtS)
{
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/Cylindrical
     */
    memcpy(_mech_rtS->Cylindrical.P1Axis, _mech_rtP + 0, sizeof(real_T) * 3);
    memcpy(_mech_rtS->Cylindrical.R1Axis, _mech_rtP + 3, sizeof(real_T) * 3);
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/Cylindrical1
     */
    memcpy(_mech_rtS->Cylindrical1.P1Axis, _mech_rtP + 6, sizeof(real_T) * 3);
    memcpy(_mech_rtS->Cylindrical1.R1Axis, _mech_rtP + 9, sizeof(real_T) * 3);
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/Revolute
     */
    memcpy(_mech_rtS->Revolute.R1Axis, _mech_rtP + 12, sizeof(real_T) * 3);
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/Revolute1
     */
    memcpy(_mech_rtS->Revolute1.R1Axis, _mech_rtP + 15, sizeof(real_T) * 3);
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/Revolute10
     */
    memcpy(_mech_rtS->Revolute10.R1Axis, _mech_rtP + 18, sizeof(real_T) * 3);
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/Revolute2
     */
    memcpy(_mech_rtS->Revolute2.R1Axis, _mech_rtP + 21, sizeof(real_T) * 3);
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/Revolute3
     */
    memcpy(_mech_rtS->Revolute3.R1Axis, _mech_rtP + 24, sizeof(real_T) * 3);
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/Revolute4
     */
    memcpy(_mech_rtS->Revolute4.R1Axis, _mech_rtP + 27, sizeof(real_T) * 3);
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/Revolute5
     */
    memcpy(_mech_rtS->Revolute5.R1Axis, _mech_rtP + 30, sizeof(real_T) * 3);
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/Revolute6
     */
    memcpy(_mech_rtS->Revolute6.R1Axis, _mech_rtP + 33, sizeof(real_T) * 3);
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/Revolute7
     */
    memcpy(_mech_rtS->Revolute7.R1Axis, _mech_rtP + 36, sizeof(real_T) * 3);
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/Revolute8
     */
    memcpy(_mech_rtS->Revolute8.R1Axis, _mech_rtP + 39, sizeof(real_T) * 3);
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/Revolute9
     */
    memcpy(_mech_rtS->Revolute9.R1Axis, _mech_rtP + 42, sizeof(real_T) * 3);
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/RootGround
     */
    memcpy(_mech_rtS->RootGround.CoordPosition, _mech_rtP + 45, sizeof(real_T) * 3);
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/RootPart
     */
    memcpy(_mech_rtS->RootPart.CGPos, _mech_rtP + 48, sizeof(real_T) * 3);
    memcpy(_mech_rtS->RootPart.CGRot, _mech_rtP + 51, sizeof(real_T) * 9);
    memcpy(_mech_rtS->RootPart.CS1Pos, _mech_rtP + 70, sizeof(real_T) * 3);
    memcpy(_mech_rtS->RootPart.CS1Rot, _mech_rtP + 73, sizeof(real_T) * 9);
    memcpy(_mech_rtS->RootPart.CS2Pos, _mech_rtP + 82, sizeof(real_T) * 3);
    memcpy(_mech_rtS->RootPart.CS2Rot, _mech_rtP + 85, sizeof(real_T) * 9);
    memcpy(_mech_rtS->RootPart.CS3Pos, _mech_rtP + 94, sizeof(real_T) * 3);
    memcpy(_mech_rtS->RootPart.CS3Rot, _mech_rtP + 97, sizeof(real_T) * 9);
    memcpy(_mech_rtS->RootPart.Inertia, _mech_rtP + 60, sizeof(real_T) * 9);
    _mech_rtS->RootPart.Mass = _mech_rtP[69];
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/W01_2-2
     */
    memcpy(_mech_rtS->W01_2_2.CGPos, _mech_rtP + 106, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W01_2_2.CGRot, _mech_rtP + 109, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W01_2_2.CS1Pos, _mech_rtP + 128, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W01_2_2.CS1Rot, _mech_rtP + 131, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W01_2_2.CS2Pos, _mech_rtP + 140, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W01_2_2.CS2Rot, _mech_rtP + 143, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W01_2_2.CS3Pos, _mech_rtP + 152, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W01_2_2.CS3Rot, _mech_rtP + 155, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W01_2_2.Inertia, _mech_rtP + 118, sizeof(real_T) * 9);
    _mech_rtS->W01_2_2.Mass = _mech_rtP[127];
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/W02_1-3
     */
    memcpy(_mech_rtS->W02_1_3.CGPos, _mech_rtP + 164, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W02_1_3.CGRot, _mech_rtP + 167, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W02_1_3.CS1Pos, _mech_rtP + 186, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W02_1_3.CS1Rot, _mech_rtP + 189, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W02_1_3.CS2Pos, _mech_rtP + 198, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W02_1_3.CS2Rot, _mech_rtP + 201, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W02_1_3.CS3Pos, _mech_rtP + 210, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W02_1_3.CS3Rot, _mech_rtP + 213, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W02_1_3.Inertia, _mech_rtP + 176, sizeof(real_T) * 9);
    _mech_rtS->W02_1_3.Mass = _mech_rtP[185];
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/W03_1-1
     */
    memcpy(_mech_rtS->W03_1_1.CGPos, _mech_rtP + 222, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W03_1_1.CGRot, _mech_rtP + 225, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W03_1_1.CS1Pos, _mech_rtP + 244, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W03_1_1.CS1Rot, _mech_rtP + 247, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W03_1_1.CS2Pos, _mech_rtP + 256, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W03_1_1.CS2Rot, _mech_rtP + 259, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W03_1_1.CS3Pos, _mech_rtP + 268, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W03_1_1.CS3Rot, _mech_rtP + 271, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W03_1_1.CS4Pos, _mech_rtP + 280, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W03_1_1.CS4Rot, _mech_rtP + 283, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W03_1_1.Inertia, _mech_rtP + 234, sizeof(real_T) * 9);
    _mech_rtS->W03_1_1.Mass = _mech_rtP[243];
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/W04-3
     */
    memcpy(_mech_rtS->W04_3.CGPos, _mech_rtP + 292, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W04_3.CGRot, _mech_rtP + 295, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W04_3.CS1Pos, _mech_rtP + 314, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W04_3.CS1Rot, _mech_rtP + 317, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W04_3.CS2Pos, _mech_rtP + 326, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W04_3.CS2Rot, _mech_rtP + 329, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W04_3.CS3Pos, _mech_rtP + 338, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W04_3.CS3Rot, _mech_rtP + 341, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W04_3.Inertia, _mech_rtP + 304, sizeof(real_T) * 9);
    _mech_rtS->W04_3.Mass = _mech_rtP[313];
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/W05-4
     */
    memcpy(_mech_rtS->W05_4.CGPos, _mech_rtP + 350, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W05_4.CGRot, _mech_rtP + 353, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W05_4.CS1Pos, _mech_rtP + 372, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W05_4.CS1Rot, _mech_rtP + 375, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W05_4.CS2Pos, _mech_rtP + 384, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W05_4.CS2Rot, _mech_rtP + 387, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W05_4.CS3Pos, _mech_rtP + 396, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W05_4.CS3Rot, _mech_rtP + 399, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W05_4.Inertia, _mech_rtP + 362, sizeof(real_T) * 9);
    _mech_rtS->W05_4.Mass = _mech_rtP[371];
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/W06-4
     */
    memcpy(_mech_rtS->W06_4.CGPos, _mech_rtP + 408, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W06_4.CGRot, _mech_rtP + 411, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W06_4.CS1Pos, _mech_rtP + 430, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W06_4.CS1Rot, _mech_rtP + 433, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W06_4.CS2Pos, _mech_rtP + 442, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W06_4.CS2Rot, _mech_rtP + 445, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W06_4.CS3Pos, _mech_rtP + 454, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W06_4.CS3Rot, _mech_rtP + 457, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W06_4.CS4Pos, _mech_rtP + 466, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W06_4.CS4Rot, _mech_rtP + 469, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W06_4.CS5Pos, _mech_rtP + 478, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W06_4.CS5Rot, _mech_rtP + 481, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W06_4.CS6Pos, _mech_rtP + 490, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W06_4.CS6Rot, _mech_rtP + 493, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W06_4.Inertia, _mech_rtP + 420, sizeof(real_T) * 9);
    _mech_rtS->W06_4.Mass = _mech_rtP[429];
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/W07-10
     */
    memcpy(_mech_rtS->W07_10.CGPos, _mech_rtP + 502, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W07_10.CGRot, _mech_rtP + 505, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W07_10.CS1Pos, _mech_rtP + 524, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W07_10.CS1Rot, _mech_rtP + 527, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W07_10.CS2Pos, _mech_rtP + 536, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W07_10.CS2Rot, _mech_rtP + 539, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W07_10.CS3Pos, _mech_rtP + 548, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W07_10.CS3Rot, _mech_rtP + 551, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W07_10.Inertia, _mech_rtP + 514, sizeof(real_T) * 9);
    _mech_rtS->W07_10.Mass = _mech_rtP[523];
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/W07-11
     */
    memcpy(_mech_rtS->W07_11.CGPos, _mech_rtP + 560, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W07_11.CGRot, _mech_rtP + 563, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W07_11.CS1Pos, _mech_rtP + 582, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W07_11.CS1Rot, _mech_rtP + 585, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W07_11.CS2Pos, _mech_rtP + 594, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W07_11.CS2Rot, _mech_rtP + 597, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W07_11.CS3Pos, _mech_rtP + 606, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W07_11.CS3Rot, _mech_rtP + 609, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W07_11.Inertia, _mech_rtP + 572, sizeof(real_T) * 9);
    _mech_rtS->W07_11.Mass = _mech_rtP[581];
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/W07-12
     */
    memcpy(_mech_rtS->W07_12.CGPos, _mech_rtP + 618, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W07_12.CGRot, _mech_rtP + 621, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W07_12.CS1Pos, _mech_rtP + 640, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W07_12.CS1Rot, _mech_rtP + 643, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W07_12.CS2Pos, _mech_rtP + 652, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W07_12.CS2Rot, _mech_rtP + 655, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W07_12.CS3Pos, _mech_rtP + 664, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W07_12.CS3Rot, _mech_rtP + 667, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W07_12.Inertia, _mech_rtP + 630, sizeof(real_T) * 9);
    _mech_rtS->W07_12.Mass = _mech_rtP[639];
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/W07-9
     */
    memcpy(_mech_rtS->W07_9.CGPos, _mech_rtP + 676, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W07_9.CGRot, _mech_rtP + 679, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W07_9.CS1Pos, _mech_rtP + 698, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W07_9.CS1Rot, _mech_rtP + 701, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W07_9.CS2Pos, _mech_rtP + 710, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W07_9.CS2Rot, _mech_rtP + 713, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W07_9.CS3Pos, _mech_rtP + 722, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W07_9.CS3Rot, _mech_rtP + 725, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W07_9.Inertia, _mech_rtP + 688, sizeof(real_T) * 9);
    _mech_rtS->W07_9.Mass = _mech_rtP[697];
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/W08-5
     */
    memcpy(_mech_rtS->W08_5.CGPos, _mech_rtP + 734, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W08_5.CGRot, _mech_rtP + 737, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W08_5.CS1Pos, _mech_rtP + 756, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W08_5.CS1Rot, _mech_rtP + 759, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W08_5.CS2Pos, _mech_rtP + 768, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W08_5.CS2Rot, _mech_rtP + 771, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W08_5.CS3Pos, _mech_rtP + 780, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W08_5.CS3Rot, _mech_rtP + 783, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W08_5.Inertia, _mech_rtP + 746, sizeof(real_T) * 9);
    _mech_rtS->W08_5.Mass = _mech_rtP[755];
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/W08-6
     */
    memcpy(_mech_rtS->W08_6.CGPos, _mech_rtP + 792, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W08_6.CGRot, _mech_rtP + 795, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W08_6.CS1Pos, _mech_rtP + 814, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W08_6.CS1Rot, _mech_rtP + 817, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W08_6.CS2Pos, _mech_rtP + 826, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W08_6.CS2Rot, _mech_rtP + 829, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W08_6.CS3Pos, _mech_rtP + 838, sizeof(real_T) * 3);
    memcpy(_mech_rtS->W08_6.CS3Rot, _mech_rtP + 841, sizeof(real_T) * 9);
    memcpy(_mech_rtS->W08_6.Inertia, _mech_rtP + 804, sizeof(real_T) * 9);
    _mech_rtS->W08_6.Mass = _mech_rtP[813];
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/Weld
     */
    memcpy(_mech_rtS->Weld.WAxis, _mech_rtP + 850, sizeof(real_T) * 3);
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/Weld1
     */
    memcpy(_mech_rtS->Weld1.WAxis, _mech_rtP + 853, sizeof(real_T) * 3);
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/Weld2
     */
    memcpy(_mech_rtS->Weld2.WAxis, _mech_rtP + 856, sizeof(real_T) * 3);
    /*
     * get runtime parameters for block:
     *     MICROBOT_1/board-1
     */
    memcpy(_mech_rtS->board_1.CGPos, _mech_rtP + 859, sizeof(real_T) * 3);
    memcpy(_mech_rtS->board_1.CGRot, _mech_rtP + 862, sizeof(real_T) * 9);
    memcpy(_mech_rtS->board_1.CS1Pos, _mech_rtP + 881, sizeof(real_T) * 3);
    memcpy(_mech_rtS->board_1.CS1Rot, _mech_rtP + 884, sizeof(real_T) * 9);
    memcpy(_mech_rtS->board_1.CS2Pos, _mech_rtP + 893, sizeof(real_T) * 3);
    memcpy(_mech_rtS->board_1.CS2Rot, _mech_rtP + 896, sizeof(real_T) * 9);
    memcpy(_mech_rtS->board_1.Inertia, _mech_rtP + 871, sizeof(real_T) * 9);
    _mech_rtS->board_1.Mass = _mech_rtP[880];
}

/*
 * Convert structure for machine to runtime parameter vector
 */
void rt_machine_parameters_to_vector_MICROBOT_1_e2dc272(const MachineParameters_MICROBOT_1_e2dc272 *_mech_rtS, real_T *_mech_rtP)
{
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/Cylindrical
     */
    memcpy(_mech_rtP + 0, _mech_rtS->Cylindrical.P1Axis, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 3, _mech_rtS->Cylindrical.R1Axis, sizeof(real_T) * 3);
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/Cylindrical1
     */
    memcpy(_mech_rtP + 6, _mech_rtS->Cylindrical1.P1Axis, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 9, _mech_rtS->Cylindrical1.R1Axis, sizeof(real_T) * 3);
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/Revolute
     */
    memcpy(_mech_rtP + 12, _mech_rtS->Revolute.R1Axis, sizeof(real_T) * 3);
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/Revolute1
     */
    memcpy(_mech_rtP + 15, _mech_rtS->Revolute1.R1Axis, sizeof(real_T) * 3);
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/Revolute10
     */
    memcpy(_mech_rtP + 18, _mech_rtS->Revolute10.R1Axis, sizeof(real_T) * 3);
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/Revolute2
     */
    memcpy(_mech_rtP + 21, _mech_rtS->Revolute2.R1Axis, sizeof(real_T) * 3);
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/Revolute3
     */
    memcpy(_mech_rtP + 24, _mech_rtS->Revolute3.R1Axis, sizeof(real_T) * 3);
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/Revolute4
     */
    memcpy(_mech_rtP + 27, _mech_rtS->Revolute4.R1Axis, sizeof(real_T) * 3);
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/Revolute5
     */
    memcpy(_mech_rtP + 30, _mech_rtS->Revolute5.R1Axis, sizeof(real_T) * 3);
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/Revolute6
     */
    memcpy(_mech_rtP + 33, _mech_rtS->Revolute6.R1Axis, sizeof(real_T) * 3);
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/Revolute7
     */
    memcpy(_mech_rtP + 36, _mech_rtS->Revolute7.R1Axis, sizeof(real_T) * 3);
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/Revolute8
     */
    memcpy(_mech_rtP + 39, _mech_rtS->Revolute8.R1Axis, sizeof(real_T) * 3);
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/Revolute9
     */
    memcpy(_mech_rtP + 42, _mech_rtS->Revolute9.R1Axis, sizeof(real_T) * 3);
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/RootGround
     */
    memcpy(_mech_rtP + 45, _mech_rtS->RootGround.CoordPosition, sizeof(real_T) * 3);
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/RootPart
     */
    memcpy(_mech_rtP + 48, _mech_rtS->RootPart.CGPos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 51, _mech_rtS->RootPart.CGRot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 70, _mech_rtS->RootPart.CS1Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 73, _mech_rtS->RootPart.CS1Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 82, _mech_rtS->RootPart.CS2Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 85, _mech_rtS->RootPart.CS2Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 94, _mech_rtS->RootPart.CS3Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 97, _mech_rtS->RootPart.CS3Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 60, _mech_rtS->RootPart.Inertia, sizeof(real_T) * 9);
    _mech_rtP[69] = _mech_rtS->RootPart.Mass;
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/W01_2-2
     */
    memcpy(_mech_rtP + 106, _mech_rtS->W01_2_2.CGPos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 109, _mech_rtS->W01_2_2.CGRot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 128, _mech_rtS->W01_2_2.CS1Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 131, _mech_rtS->W01_2_2.CS1Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 140, _mech_rtS->W01_2_2.CS2Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 143, _mech_rtS->W01_2_2.CS2Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 152, _mech_rtS->W01_2_2.CS3Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 155, _mech_rtS->W01_2_2.CS3Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 118, _mech_rtS->W01_2_2.Inertia, sizeof(real_T) * 9);
    _mech_rtP[127] = _mech_rtS->W01_2_2.Mass;
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/W02_1-3
     */
    memcpy(_mech_rtP + 164, _mech_rtS->W02_1_3.CGPos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 167, _mech_rtS->W02_1_3.CGRot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 186, _mech_rtS->W02_1_3.CS1Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 189, _mech_rtS->W02_1_3.CS1Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 198, _mech_rtS->W02_1_3.CS2Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 201, _mech_rtS->W02_1_3.CS2Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 210, _mech_rtS->W02_1_3.CS3Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 213, _mech_rtS->W02_1_3.CS3Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 176, _mech_rtS->W02_1_3.Inertia, sizeof(real_T) * 9);
    _mech_rtP[185] = _mech_rtS->W02_1_3.Mass;
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/W03_1-1
     */
    memcpy(_mech_rtP + 222, _mech_rtS->W03_1_1.CGPos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 225, _mech_rtS->W03_1_1.CGRot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 244, _mech_rtS->W03_1_1.CS1Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 247, _mech_rtS->W03_1_1.CS1Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 256, _mech_rtS->W03_1_1.CS2Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 259, _mech_rtS->W03_1_1.CS2Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 268, _mech_rtS->W03_1_1.CS3Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 271, _mech_rtS->W03_1_1.CS3Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 280, _mech_rtS->W03_1_1.CS4Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 283, _mech_rtS->W03_1_1.CS4Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 234, _mech_rtS->W03_1_1.Inertia, sizeof(real_T) * 9);
    _mech_rtP[243] = _mech_rtS->W03_1_1.Mass;
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/W04-3
     */
    memcpy(_mech_rtP + 292, _mech_rtS->W04_3.CGPos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 295, _mech_rtS->W04_3.CGRot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 314, _mech_rtS->W04_3.CS1Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 317, _mech_rtS->W04_3.CS1Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 326, _mech_rtS->W04_3.CS2Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 329, _mech_rtS->W04_3.CS2Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 338, _mech_rtS->W04_3.CS3Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 341, _mech_rtS->W04_3.CS3Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 304, _mech_rtS->W04_3.Inertia, sizeof(real_T) * 9);
    _mech_rtP[313] = _mech_rtS->W04_3.Mass;
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/W05-4
     */
    memcpy(_mech_rtP + 350, _mech_rtS->W05_4.CGPos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 353, _mech_rtS->W05_4.CGRot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 372, _mech_rtS->W05_4.CS1Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 375, _mech_rtS->W05_4.CS1Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 384, _mech_rtS->W05_4.CS2Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 387, _mech_rtS->W05_4.CS2Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 396, _mech_rtS->W05_4.CS3Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 399, _mech_rtS->W05_4.CS3Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 362, _mech_rtS->W05_4.Inertia, sizeof(real_T) * 9);
    _mech_rtP[371] = _mech_rtS->W05_4.Mass;
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/W06-4
     */
    memcpy(_mech_rtP + 408, _mech_rtS->W06_4.CGPos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 411, _mech_rtS->W06_4.CGRot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 430, _mech_rtS->W06_4.CS1Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 433, _mech_rtS->W06_4.CS1Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 442, _mech_rtS->W06_4.CS2Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 445, _mech_rtS->W06_4.CS2Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 454, _mech_rtS->W06_4.CS3Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 457, _mech_rtS->W06_4.CS3Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 466, _mech_rtS->W06_4.CS4Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 469, _mech_rtS->W06_4.CS4Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 478, _mech_rtS->W06_4.CS5Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 481, _mech_rtS->W06_4.CS5Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 490, _mech_rtS->W06_4.CS6Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 493, _mech_rtS->W06_4.CS6Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 420, _mech_rtS->W06_4.Inertia, sizeof(real_T) * 9);
    _mech_rtP[429] = _mech_rtS->W06_4.Mass;
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/W07-10
     */
    memcpy(_mech_rtP + 502, _mech_rtS->W07_10.CGPos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 505, _mech_rtS->W07_10.CGRot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 524, _mech_rtS->W07_10.CS1Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 527, _mech_rtS->W07_10.CS1Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 536, _mech_rtS->W07_10.CS2Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 539, _mech_rtS->W07_10.CS2Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 548, _mech_rtS->W07_10.CS3Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 551, _mech_rtS->W07_10.CS3Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 514, _mech_rtS->W07_10.Inertia, sizeof(real_T) * 9);
    _mech_rtP[523] = _mech_rtS->W07_10.Mass;
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/W07-11
     */
    memcpy(_mech_rtP + 560, _mech_rtS->W07_11.CGPos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 563, _mech_rtS->W07_11.CGRot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 582, _mech_rtS->W07_11.CS1Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 585, _mech_rtS->W07_11.CS1Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 594, _mech_rtS->W07_11.CS2Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 597, _mech_rtS->W07_11.CS2Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 606, _mech_rtS->W07_11.CS3Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 609, _mech_rtS->W07_11.CS3Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 572, _mech_rtS->W07_11.Inertia, sizeof(real_T) * 9);
    _mech_rtP[581] = _mech_rtS->W07_11.Mass;
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/W07-12
     */
    memcpy(_mech_rtP + 618, _mech_rtS->W07_12.CGPos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 621, _mech_rtS->W07_12.CGRot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 640, _mech_rtS->W07_12.CS1Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 643, _mech_rtS->W07_12.CS1Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 652, _mech_rtS->W07_12.CS2Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 655, _mech_rtS->W07_12.CS2Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 664, _mech_rtS->W07_12.CS3Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 667, _mech_rtS->W07_12.CS3Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 630, _mech_rtS->W07_12.Inertia, sizeof(real_T) * 9);
    _mech_rtP[639] = _mech_rtS->W07_12.Mass;
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/W07-9
     */
    memcpy(_mech_rtP + 676, _mech_rtS->W07_9.CGPos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 679, _mech_rtS->W07_9.CGRot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 698, _mech_rtS->W07_9.CS1Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 701, _mech_rtS->W07_9.CS1Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 710, _mech_rtS->W07_9.CS2Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 713, _mech_rtS->W07_9.CS2Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 722, _mech_rtS->W07_9.CS3Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 725, _mech_rtS->W07_9.CS3Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 688, _mech_rtS->W07_9.Inertia, sizeof(real_T) * 9);
    _mech_rtP[697] = _mech_rtS->W07_9.Mass;
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/W08-5
     */
    memcpy(_mech_rtP + 734, _mech_rtS->W08_5.CGPos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 737, _mech_rtS->W08_5.CGRot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 756, _mech_rtS->W08_5.CS1Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 759, _mech_rtS->W08_5.CS1Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 768, _mech_rtS->W08_5.CS2Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 771, _mech_rtS->W08_5.CS2Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 780, _mech_rtS->W08_5.CS3Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 783, _mech_rtS->W08_5.CS3Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 746, _mech_rtS->W08_5.Inertia, sizeof(real_T) * 9);
    _mech_rtP[755] = _mech_rtS->W08_5.Mass;
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/W08-6
     */
    memcpy(_mech_rtP + 792, _mech_rtS->W08_6.CGPos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 795, _mech_rtS->W08_6.CGRot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 814, _mech_rtS->W08_6.CS1Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 817, _mech_rtS->W08_6.CS1Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 826, _mech_rtS->W08_6.CS2Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 829, _mech_rtS->W08_6.CS2Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 838, _mech_rtS->W08_6.CS3Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 841, _mech_rtS->W08_6.CS3Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 804, _mech_rtS->W08_6.Inertia, sizeof(real_T) * 9);
    _mech_rtP[813] = _mech_rtS->W08_6.Mass;
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/Weld
     */
    memcpy(_mech_rtP + 850, _mech_rtS->Weld.WAxis, sizeof(real_T) * 3);
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/Weld1
     */
    memcpy(_mech_rtP + 853, _mech_rtS->Weld1.WAxis, sizeof(real_T) * 3);
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/Weld2
     */
    memcpy(_mech_rtP + 856, _mech_rtS->Weld2.WAxis, sizeof(real_T) * 3);
    /*
     * arrange runtime parameters for block:
     *     MICROBOT_1/board-1
     */
    memcpy(_mech_rtP + 859, _mech_rtS->board_1.CGPos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 862, _mech_rtS->board_1.CGRot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 881, _mech_rtS->board_1.CS1Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 884, _mech_rtS->board_1.CS1Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 893, _mech_rtS->board_1.CS2Pos, sizeof(real_T) * 3);
    memcpy(_mech_rtP + 896, _mech_rtS->board_1.CS2Rot, sizeof(real_T) * 9);
    memcpy(_mech_rtP + 871, _mech_rtS->board_1.Inertia, sizeof(real_T) * 9);
    _mech_rtP[880] = _mech_rtS->board_1.Mass;
}

/* [EOF] rt_mechanism_data.c */
