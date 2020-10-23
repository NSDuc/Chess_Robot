/*
 * MICROBOT_1.h
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

#ifndef RTW_HEADER_MICROBOT_1_h_
#define RTW_HEADER_MICROBOT_1_h_
#include <float.h>
#include <string.h>
#include <stddef.h>
#ifndef MICROBOT_1_COMMON_INCLUDES_
# define MICROBOT_1_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "rtw_continuous.h"
#include "rtw_solver.h"
#include "rt_logging.h"
#endif                                 /* MICROBOT_1_COMMON_INCLUDES_ */

#include "MICROBOT_1_types.h"

/* Shared type includes */
#include "multiword_types.h"
#include "rt_nonfinite.h"

/* Macros for accessing real-time model data structure */
#ifndef rtmGetBlkStateChangeFlag
# define rtmGetBlkStateChangeFlag(rtm) ((rtm)->ModelData.blkStateChange)
#endif

#ifndef rtmSetBlkStateChangeFlag
# define rtmSetBlkStateChangeFlag(rtm, val) ((rtm)->ModelData.blkStateChange = (val))
#endif

#ifndef rtmGetContStateDisabled
# define rtmGetContStateDisabled(rtm)  ((rtm)->ModelData.contStateDisabled)
#endif

#ifndef rtmSetContStateDisabled
# define rtmSetContStateDisabled(rtm, val) ((rtm)->ModelData.contStateDisabled = (val))
#endif

#ifndef rtmGetContStates
# define rtmGetContStates(rtm)         ((rtm)->ModelData.contStates)
#endif

#ifndef rtmSetContStates
# define rtmSetContStates(rtm, val)    ((rtm)->ModelData.contStates = (val))
#endif

#ifndef rtmGetDerivCacheNeedsReset
# define rtmGetDerivCacheNeedsReset(rtm) ((rtm)->ModelData.derivCacheNeedsReset)
#endif

#ifndef rtmSetDerivCacheNeedsReset
# define rtmSetDerivCacheNeedsReset(rtm, val) ((rtm)->ModelData.derivCacheNeedsReset = (val))
#endif

#ifndef rtmGetFinalTime
# define rtmGetFinalTime(rtm)          ((rtm)->Timing.tFinal)
#endif

#ifndef rtmGetIntgData
# define rtmGetIntgData(rtm)           ((rtm)->ModelData.intgData)
#endif

#ifndef rtmSetIntgData
# define rtmSetIntgData(rtm, val)      ((rtm)->ModelData.intgData = (val))
#endif

#ifndef rtmGetOdeF
# define rtmGetOdeF(rtm)               ((rtm)->ModelData.odeF)
#endif

#ifndef rtmSetOdeF
# define rtmSetOdeF(rtm, val)          ((rtm)->ModelData.odeF = (val))
#endif

#ifndef rtmGetOdeY
# define rtmGetOdeY(rtm)               ((rtm)->ModelData.odeY)
#endif

#ifndef rtmSetOdeY
# define rtmSetOdeY(rtm, val)          ((rtm)->ModelData.odeY = (val))
#endif

#ifndef rtmGetPeriodicContStateIndices
# define rtmGetPeriodicContStateIndices(rtm) ((rtm)->ModelData.periodicContStateIndices)
#endif

#ifndef rtmSetPeriodicContStateIndices
# define rtmSetPeriodicContStateIndices(rtm, val) ((rtm)->ModelData.periodicContStateIndices = (val))
#endif

#ifndef rtmGetPeriodicContStateRanges
# define rtmGetPeriodicContStateRanges(rtm) ((rtm)->ModelData.periodicContStateRanges)
#endif

#ifndef rtmSetPeriodicContStateRanges
# define rtmSetPeriodicContStateRanges(rtm, val) ((rtm)->ModelData.periodicContStateRanges = (val))
#endif

#ifndef rtmGetRTWLogInfo
# define rtmGetRTWLogInfo(rtm)         ((rtm)->rtwLogInfo)
#endif

#ifndef rtmGetZCCacheNeedsReset
# define rtmGetZCCacheNeedsReset(rtm)  ((rtm)->ModelData.zCCacheNeedsReset)
#endif

#ifndef rtmSetZCCacheNeedsReset
# define rtmSetZCCacheNeedsReset(rtm, val) ((rtm)->ModelData.zCCacheNeedsReset = (val))
#endif

#ifndef rtmGetdX
# define rtmGetdX(rtm)                 ((rtm)->ModelData.derivs)
#endif

#ifndef rtmSetdX
# define rtmSetdX(rtm, val)            ((rtm)->ModelData.derivs = (val))
#endif

#ifndef rtmGetErrorStatus
# define rtmGetErrorStatus(rtm)        ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
# define rtmSetErrorStatus(rtm, val)   ((rtm)->errorStatus = (val))
#endif

#ifndef rtmGetStopRequested
# define rtmGetStopRequested(rtm)      ((rtm)->Timing.stopRequestedFlag)
#endif

#ifndef rtmSetStopRequested
# define rtmSetStopRequested(rtm, val) ((rtm)->Timing.stopRequestedFlag = (val))
#endif

#ifndef rtmGetStopRequestedPtr
# define rtmGetStopRequestedPtr(rtm)   (&((rtm)->Timing.stopRequestedFlag))
#endif

#ifndef rtmGetT
# define rtmGetT(rtm)                  (rtmGetTPtr((rtm))[0])
#endif

#ifndef rtmGetTFinal
# define rtmGetTFinal(rtm)             ((rtm)->Timing.tFinal)
#endif

/* Block signals (auto storage) */
typedef struct {
  real_T SliderGain;                   /* '<S15>/Slider Gain' */
  real_T Gain;                         /* '<Root>/Gain' */
  real_T SliderGain_m;                 /* '<S11>/Slider Gain' */
  real_T SliderGain_k;                 /* '<S12>/Slider Gain' */
  real_T SliderGain_p;                 /* '<S13>/Slider Gain' */
  real_T SliderGain_i;                 /* '<S14>/Slider Gain' */
  real_T Block1_o1[8];                 /* '<S16>/Block#1' */
  real_T Block1_o2;                    /* '<S16>/Block#1' */
  real_T _gravity_conversion[3];       /* '<S16>/_gravity_conversion' */
  real_T Block2;                       /* '<S16>/Block#2' */
  real_T Block3;                       /* '<S16>/Block#3' */
} B_MICROBOT_1_T;

/* Block states (auto storage) for system '<Root>' */
typedef struct {
  void *Block1_PWORK;                  /* '<S16>/Block#1' */
  void *Block2_PWORK;                  /* '<S16>/Block#2' */
  void *Block3_PWORK;                  /* '<S16>/Block#3' */
  int_T Block1_IWORK;                  /* '<S16>/Block#1' */
  int_T Block3_IWORK;                  /* '<S16>/Block#3' */
} DW_MICROBOT_1_T;

/* Continuous states (auto storage) */
typedef struct {
  real_T Revolute9R1Position[8];       /* '<S16>/Block#1' */
} X_MICROBOT_1_T;

/* State derivatives (auto storage) */
typedef struct {
  real_T Revolute9R1Position[8];       /* '<S16>/Block#1' */
} XDot_MICROBOT_1_T;

/* State disabled  */
typedef struct {
  boolean_T Revolute9R1Position[8];    /* '<S16>/Block#1' */
} XDis_MICROBOT_1_T;

#ifndef ODE4_INTG
#define ODE4_INTG

/* ODE4 Integration Data */
typedef struct {
  real_T *y;                           /* output */
  real_T *f[4];                        /* derivatives */
} ODE4_IntgData;

#endif

/* Parameters (auto storage) */
struct P_MICROBOT_1_T_ {
  real_T MachineEnvironment_Gravity[3];/* Mask Parameter: MachineEnvironment_Gravity
                                        * Referenced by: '<S9>/SOURCE_BLOCK'
                                        */
  real_T SliderGain6_gain;             /* Mask Parameter: SliderGain6_gain
                                        * Referenced by: '<S15>/Slider Gain'
                                        */
  real_T SliderGain2_gain;             /* Mask Parameter: SliderGain2_gain
                                        * Referenced by: '<S11>/Slider Gain'
                                        */
  real_T SliderGain3_gain;             /* Mask Parameter: SliderGain3_gain
                                        * Referenced by: '<S12>/Slider Gain'
                                        */
  real_T SliderGain4_gain;             /* Mask Parameter: SliderGain4_gain
                                        * Referenced by: '<S13>/Slider Gain'
                                        */
  real_T SliderGain5_gain;             /* Mask Parameter: SliderGain5_gain
                                        * Referenced by: '<S14>/Slider Gain'
                                        */
  real_T Constant_Value;               /* Expression: 41.896
                                        * Referenced by: '<Root>/Constant'
                                        */
  real_T Constant7_Value;              /* Expression: 1
                                        * Referenced by: '<Root>/Constant7'
                                        */
  real_T Constant8_Value;              /* Expression: 1
                                        * Referenced by: '<Root>/Constant8'
                                        */
  real_T Constant1_Value;              /* Expression: -1
                                        * Referenced by: '<Root>/Constant1'
                                        */
  real_T Constant17_Value;             /* Expression: 1
                                        * Referenced by: '<Root>/Constant17'
                                        */
  real_T Constant18_Value;             /* Expression: 1
                                        * Referenced by: '<Root>/Constant18'
                                        */
  real_T Constant19_Value;             /* Expression: 1
                                        * Referenced by: '<Root>/Constant19'
                                        */
  real_T Constant20_Value;             /* Expression: 1
                                        * Referenced by: '<Root>/Constant20'
                                        */
  real_T Gain_Gain;                    /* Expression: -1
                                        * Referenced by: '<Root>/Gain'
                                        */
  real_T Constant10_Value;             /* Expression: 1
                                        * Referenced by: '<Root>/Constant10'
                                        */
  real_T Constant2_Value;              /* Expression: 1
                                        * Referenced by: '<Root>/Constant2'
                                        */
  real_T Constant9_Value;              /* Expression: 1
                                        * Referenced by: '<Root>/Constant9'
                                        */
  real_T Constant11_Value;             /* Expression: 1
                                        * Referenced by: '<Root>/Constant11'
                                        */
  real_T Constant12_Value;             /* Expression: 1
                                        * Referenced by: '<Root>/Constant12'
                                        */
  real_T Constant3_Value;              /* Expression: -1
                                        * Referenced by: '<Root>/Constant3'
                                        */
  real_T Constant13_Value;             /* Expression: 1
                                        * Referenced by: '<Root>/Constant13'
                                        */
  real_T Constant14_Value;             /* Expression: 1
                                        * Referenced by: '<Root>/Constant14'
                                        */
  real_T Constant4_Value;              /* Expression: -1
                                        * Referenced by: '<Root>/Constant4'
                                        */
  real_T Constant15_Value;             /* Expression: 1
                                        * Referenced by: '<Root>/Constant15'
                                        */
  real_T Constant16_Value;             /* Expression: 1
                                        * Referenced by: '<Root>/Constant16'
                                        */
  real_T Constant5_Value;              /* Expression: 1
                                        * Referenced by: '<Root>/Constant5'
                                        */
  real_T Constant6_Value;              /* Expression: 100
                                        * Referenced by: '<Root>/Constant6'
                                        */
  real_T Constant21_Value;             /* Expression: 10
                                        * Referenced by: '<Root>/Constant21'
                                        */
  real_T Block1_SimMechanicsRuntimeParam[905];/* Computed Parameter: Block1_SimMechanicsRuntimeParam
                                               * Referenced by: '<S16>/Block#1'
                                               */
  real_T _gravity_conversion_Gain;     /* Expression: -1
                                        * Referenced by: '<S16>/_gravity_conversion'
                                        */
};

/* Real-time Model Data Structure */
struct tag_RTM_MICROBOT_1_T {
  const char_T *errorStatus;
  RTWLogInfo *rtwLogInfo;
  RTWSolverInfo solverInfo;

  /*
   * ModelData:
   * The following substructure contains information regarding
   * the data used in the model.
   */
  struct {
    X_MICROBOT_1_T *contStates;
    int_T *periodicContStateIndices;
    real_T *periodicContStateRanges;
    real_T *derivs;
    boolean_T *contStateDisabled;
    boolean_T zCCacheNeedsReset;
    boolean_T derivCacheNeedsReset;
    boolean_T blkStateChange;
    real_T odeY[8];
    real_T odeF[4][8];
    ODE4_IntgData intgData;
  } ModelData;

  /*
   * Sizes:
   * The following substructure contains sizes information
   * for many of the model attributes such as inputs, outputs,
   * dwork, sample times, etc.
   */
  struct {
    int_T numContStates;
    int_T numPeriodicContStates;
    int_T numSampTimes;
  } Sizes;

  /*
   * Timing:
   * The following substructure contains information regarding
   * the timing information for the model.
   */
  struct {
    uint32_T clockTick0;
    uint32_T clockTickH0;
    time_T stepSize0;
    uint32_T clockTick1;
    uint32_T clockTickH1;
    boolean_T firstInitCondFlag;
    time_T tFinal;
    SimTimeStep simTimeStep;
    boolean_T stopRequestedFlag;
    time_T *t;
    time_T tArray[2];
  } Timing;
};

/* Block parameters (auto storage) */
extern P_MICROBOT_1_T MICROBOT_1_P;

/* Block signals (auto storage) */
extern B_MICROBOT_1_T MICROBOT_1_B;

/* Continuous states (auto storage) */
extern X_MICROBOT_1_T MICROBOT_1_X;

/* Block states (auto storage) */
extern DW_MICROBOT_1_T MICROBOT_1_DW;

/* Model entry point functions */
extern void MICROBOT_1_initialize(void);
extern void MICROBOT_1_step(void);
extern void MICROBOT_1_terminate(void);

/* Real-time Model object */
extern RT_MODEL_MICROBOT_1_T *const MICROBOT_1_M;

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'MICROBOT_1'
 * '<S1>'   : 'MICROBOT_1/Joint Actuator'
 * '<S2>'   : 'MICROBOT_1/Joint Actuator1'
 * '<S3>'   : 'MICROBOT_1/Joint Actuator2'
 * '<S4>'   : 'MICROBOT_1/Joint Actuator3'
 * '<S5>'   : 'MICROBOT_1/Joint Actuator4'
 * '<S6>'   : 'MICROBOT_1/Joint Actuator5'
 * '<S7>'   : 'MICROBOT_1/Joint Actuator6'
 * '<S8>'   : 'MICROBOT_1/MATLAB Function'
 * '<S9>'   : 'MICROBOT_1/Machine Environment'
 * '<S10>'  : 'MICROBOT_1/RootGround'
 * '<S11>'  : 'MICROBOT_1/Slider Gain2'
 * '<S12>'  : 'MICROBOT_1/Slider Gain3'
 * '<S13>'  : 'MICROBOT_1/Slider Gain4'
 * '<S14>'  : 'MICROBOT_1/Slider Gain5'
 * '<S15>'  : 'MICROBOT_1/Slider Gain6'
 * '<S16>'  : 'MICROBOT_1/RootGround/_mech_engine'
 * '<S17>'  : 'MICROBOT_1/RootGround/_mech_engine/actuators'
 * '<S18>'  : 'MICROBOT_1/RootGround/_mech_engine/sensors'
 * '<S19>'  : 'MICROBOT_1/RootGround/_mech_engine/actuators/stub actuators'
 * '<S20>'  : 'MICROBOT_1/RootGround/_mech_engine/sensors/stub sensors'
 */
#endif                                 /* RTW_HEADER_MICROBOT_1_h_ */
