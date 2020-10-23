/*
 * MICROBOT_1_private.h
 *
 * Code generation for model "MICROBOT_1".
 *
 * Model version              : 1.25
 * Simulink Coder version : 8.8 (R2015a) 09-Feb-2015
 * C source code generated on : Fri Oct 23 09:41:03 2020
 *
 * Target selection: grt.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: 32-bit Generic
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef RTW_HEADER_MICROBOT_1_private_h_
#define RTW_HEADER_MICROBOT_1_private_h_
#include "rtwtypes.h"
#include "builtin_typeid_types.h"
#include "multiword_types.h"

/* Private macros used by the generated code to access rtModel */
#ifndef rtmSetFirstInitCond
# define rtmSetFirstInitCond(rtm, val) ((rtm)->Timing.firstInitCondFlag = (val))
#endif

#ifndef rtmIsFirstInitCond
# define rtmIsFirstInitCond(rtm)       ((rtm)->Timing.firstInitCondFlag)
#endif

#ifndef rtmIsMajorTimeStep
# define rtmIsMajorTimeStep(rtm)       (((rtm)->Timing.simTimeStep) == MAJOR_TIME_STEP)
#endif

#ifndef rtmIsMinorTimeStep
# define rtmIsMinorTimeStep(rtm)       (((rtm)->Timing.simTimeStep) == MINOR_TIME_STEP)
#endif

#ifndef rtmSetTFinal
# define rtmSetTFinal(rtm, val)        ((rtm)->Timing.tFinal = (val))
#endif

#ifndef rtmGetTPtr
# define rtmGetTPtr(rtm)               ((rtm)->Timing.t)
#endif

#ifndef rtmSetTPtr
# define rtmSetTPtr(rtm, val)          ((rtm)->Timing.t = (val))
#endif

#include "mech_std.h"
#include "mtypes.h"
#include "simulation_data.h"
#include "mech_method_table.h"
#include "rt_mechanism.h"
#include "sim_mechanics_imports.h"

/*
 * simulation data structure for SimMechanics, one for each SFunction
 */
typedef struct {
  Mechanism *mechanism;
  SimulationDataGeneral genSimData;
  SimulationDataOutputs outSimData;
} _rtMech_PWORK;

/* private model entry point functions */
extern void MICROBOT_1_derivatives(void);

#endif                                 /* RTW_HEADER_MICROBOT_1_private_h_ */
