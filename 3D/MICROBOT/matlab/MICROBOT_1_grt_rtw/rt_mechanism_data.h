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
#ifndef rt_mechanism_data_h
#define rt_mechanism_data_h
/*
 * SimMechanics run-time data structure for machine:
 *     MICROBOT_1/RootGround
 */
typedef struct {
    /*
     * run-time parameters for block:
     *     MICROBOT_1/Cylindrical
     */
    struct {
        real_T    P1Axis[3];
        real_T    R1Axis[3];
    } Cylindrical;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/Cylindrical1
     */
    struct {
        real_T    P1Axis[3];
        real_T    R1Axis[3];
    } Cylindrical1;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/Revolute
     */
    struct {
        real_T    R1Axis[3];
    } Revolute;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/Revolute1
     */
    struct {
        real_T    R1Axis[3];
    } Revolute1;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/Revolute10
     */
    struct {
        real_T    R1Axis[3];
    } Revolute10;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/Revolute2
     */
    struct {
        real_T    R1Axis[3];
    } Revolute2;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/Revolute3
     */
    struct {
        real_T    R1Axis[3];
    } Revolute3;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/Revolute4
     */
    struct {
        real_T    R1Axis[3];
    } Revolute4;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/Revolute5
     */
    struct {
        real_T    R1Axis[3];
    } Revolute5;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/Revolute6
     */
    struct {
        real_T    R1Axis[3];
    } Revolute6;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/Revolute7
     */
    struct {
        real_T    R1Axis[3];
    } Revolute7;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/Revolute8
     */
    struct {
        real_T    R1Axis[3];
    } Revolute8;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/Revolute9
     */
    struct {
        real_T    R1Axis[3];
    } Revolute9;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/RootGround
     */
    struct {
        real_T    CoordPosition[3];
    } RootGround;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/RootPart
     */
    struct {
        real_T    CGPos[3];
        real_T    CGRot[9];
        real_T    CS1Pos[3];
        real_T    CS1Rot[9];
        real_T    CS2Pos[3];
        real_T    CS2Rot[9];
        real_T    CS3Pos[3];
        real_T    CS3Rot[9];
        real_T    Inertia[9];
        real_T    Mass;
    } RootPart;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/W01_2-2
     */
    struct {
        real_T    CGPos[3];
        real_T    CGRot[9];
        real_T    CS1Pos[3];
        real_T    CS1Rot[9];
        real_T    CS2Pos[3];
        real_T    CS2Rot[9];
        real_T    CS3Pos[3];
        real_T    CS3Rot[9];
        real_T    Inertia[9];
        real_T    Mass;
    } W01_2_2;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/W02_1-3
     */
    struct {
        real_T    CGPos[3];
        real_T    CGRot[9];
        real_T    CS1Pos[3];
        real_T    CS1Rot[9];
        real_T    CS2Pos[3];
        real_T    CS2Rot[9];
        real_T    CS3Pos[3];
        real_T    CS3Rot[9];
        real_T    Inertia[9];
        real_T    Mass;
    } W02_1_3;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/W03_1-1
     */
    struct {
        real_T    CGPos[3];
        real_T    CGRot[9];
        real_T    CS1Pos[3];
        real_T    CS1Rot[9];
        real_T    CS2Pos[3];
        real_T    CS2Rot[9];
        real_T    CS3Pos[3];
        real_T    CS3Rot[9];
        real_T    CS4Pos[3];
        real_T    CS4Rot[9];
        real_T    Inertia[9];
        real_T    Mass;
    } W03_1_1;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/W04-3
     */
    struct {
        real_T    CGPos[3];
        real_T    CGRot[9];
        real_T    CS1Pos[3];
        real_T    CS1Rot[9];
        real_T    CS2Pos[3];
        real_T    CS2Rot[9];
        real_T    CS3Pos[3];
        real_T    CS3Rot[9];
        real_T    Inertia[9];
        real_T    Mass;
    } W04_3;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/W05-4
     */
    struct {
        real_T    CGPos[3];
        real_T    CGRot[9];
        real_T    CS1Pos[3];
        real_T    CS1Rot[9];
        real_T    CS2Pos[3];
        real_T    CS2Rot[9];
        real_T    CS3Pos[3];
        real_T    CS3Rot[9];
        real_T    Inertia[9];
        real_T    Mass;
    } W05_4;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/W06-4
     */
    struct {
        real_T    CGPos[3];
        real_T    CGRot[9];
        real_T    CS1Pos[3];
        real_T    CS1Rot[9];
        real_T    CS2Pos[3];
        real_T    CS2Rot[9];
        real_T    CS3Pos[3];
        real_T    CS3Rot[9];
        real_T    CS4Pos[3];
        real_T    CS4Rot[9];
        real_T    CS5Pos[3];
        real_T    CS5Rot[9];
        real_T    CS6Pos[3];
        real_T    CS6Rot[9];
        real_T    Inertia[9];
        real_T    Mass;
    } W06_4;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/W07-10
     */
    struct {
        real_T    CGPos[3];
        real_T    CGRot[9];
        real_T    CS1Pos[3];
        real_T    CS1Rot[9];
        real_T    CS2Pos[3];
        real_T    CS2Rot[9];
        real_T    CS3Pos[3];
        real_T    CS3Rot[9];
        real_T    Inertia[9];
        real_T    Mass;
    } W07_10;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/W07-11
     */
    struct {
        real_T    CGPos[3];
        real_T    CGRot[9];
        real_T    CS1Pos[3];
        real_T    CS1Rot[9];
        real_T    CS2Pos[3];
        real_T    CS2Rot[9];
        real_T    CS3Pos[3];
        real_T    CS3Rot[9];
        real_T    Inertia[9];
        real_T    Mass;
    } W07_11;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/W07-12
     */
    struct {
        real_T    CGPos[3];
        real_T    CGRot[9];
        real_T    CS1Pos[3];
        real_T    CS1Rot[9];
        real_T    CS2Pos[3];
        real_T    CS2Rot[9];
        real_T    CS3Pos[3];
        real_T    CS3Rot[9];
        real_T    Inertia[9];
        real_T    Mass;
    } W07_12;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/W07-9
     */
    struct {
        real_T    CGPos[3];
        real_T    CGRot[9];
        real_T    CS1Pos[3];
        real_T    CS1Rot[9];
        real_T    CS2Pos[3];
        real_T    CS2Rot[9];
        real_T    CS3Pos[3];
        real_T    CS3Rot[9];
        real_T    Inertia[9];
        real_T    Mass;
    } W07_9;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/W08-5
     */
    struct {
        real_T    CGPos[3];
        real_T    CGRot[9];
        real_T    CS1Pos[3];
        real_T    CS1Rot[9];
        real_T    CS2Pos[3];
        real_T    CS2Rot[9];
        real_T    CS3Pos[3];
        real_T    CS3Rot[9];
        real_T    Inertia[9];
        real_T    Mass;
    } W08_5;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/W08-6
     */
    struct {
        real_T    CGPos[3];
        real_T    CGRot[9];
        real_T    CS1Pos[3];
        real_T    CS1Rot[9];
        real_T    CS2Pos[3];
        real_T    CS2Rot[9];
        real_T    CS3Pos[3];
        real_T    CS3Rot[9];
        real_T    Inertia[9];
        real_T    Mass;
    } W08_6;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/Weld
     */
    struct {
        real_T    WAxis[3];
    } Weld;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/Weld1
     */
    struct {
        real_T    WAxis[3];
    } Weld1;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/Weld2
     */
    struct {
        real_T    WAxis[3];
    } Weld2;
    /*
     * run-time parameters for block:
     *     MICROBOT_1/board-1
     */
    struct {
        real_T    CGPos[3];
        real_T    CGRot[9];
        real_T    CS1Pos[3];
        real_T    CS1Rot[9];
        real_T    CS2Pos[3];
        real_T    CS2Rot[9];
        real_T    Inertia[9];
        real_T    Mass;
    } board_1;
} MachineParameters_MICROBOT_1_e2dc272;
extern void rt_vector_to_machine_parameters_MICROBOT_1_e2dc272(const real_T *, MachineParameters_MICROBOT_1_e2dc272 *);
extern void rt_machine_parameters_to_vector_MICROBOT_1_e2dc272(const MachineParameters_MICROBOT_1_e2dc272 *, real_T *);


#endif /* rt_mechanism_data_h */
/* [EOF] rt_mechanism_data.h */
