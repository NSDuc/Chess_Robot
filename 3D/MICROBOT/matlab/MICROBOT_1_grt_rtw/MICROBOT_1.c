/*
 * MICROBOT_1.c
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

#include "MICROBOT_1.h"
#include "MICROBOT_1_private.h"

/* Block signals (auto storage) */
B_MICROBOT_1_T MICROBOT_1_B;

/* Continuous states */
X_MICROBOT_1_T MICROBOT_1_X;

/* Block states (auto storage) */
DW_MICROBOT_1_T MICROBOT_1_DW;

/* Real-time model */
RT_MODEL_MICROBOT_1_T MICROBOT_1_M_;
RT_MODEL_MICROBOT_1_T *const MICROBOT_1_M = &MICROBOT_1_M_;

/* Projection for root system: '<Root>' */
void MICROBOT_1_projection(void)
{
  /* S-Function Block: <S16>/Block#1 */
  {
    _rtMech_PWORK *mechWork = (_rtMech_PWORK *) MICROBOT_1_DW.Block1_PWORK;
    mechWork->genSimData.time = MICROBOT_1_M->Timing.t[0];
    if (sFcnProjectionMethod(mechWork->mechanism,&(mechWork->genSimData))) {
      {
        const ErrorRecord *err = mech_getErrorMsg();
        static char_T errorMsg[1024];
        sprintf(errorMsg,
                err->errorMsg,
                err->blocks[0],
                err->blocks[1],
                err->blocks[2],
                err->blocks[3],
                err->blocks[4]);
        rtmSetErrorStatus(MICROBOT_1_M, errorMsg);
        return;
      }
    }
  }
}

/*
 * This function updates continuous states using the ODE4 fixed-step
 * solver algorithm
 */
static void rt_ertODEUpdateContinuousStates(RTWSolverInfo *si )
{
  time_T t = rtsiGetT(si);
  time_T tnew = rtsiGetSolverStopTime(si);
  time_T h = rtsiGetStepSize(si);
  real_T *x = rtsiGetContStates(si);
  ODE4_IntgData *id = (ODE4_IntgData *)rtsiGetSolverData(si);
  real_T *y = id->y;
  real_T *f0 = id->f[0];
  real_T *f1 = id->f[1];
  real_T *f2 = id->f[2];
  real_T *f3 = id->f[3];
  real_T temp;
  int_T i;
  int_T nXc = 8;
  rtsiSetSimTimeStep(si,MINOR_TIME_STEP);

  /* Save the state values at time t in y, we'll use x as ynew. */
  (void) memcpy(y, x,
                (uint_T)nXc*sizeof(real_T));

  /* Assumes that rtsiSetT and ModelOutputs are up-to-date */
  /* f0 = f(t,y) */
  rtsiSetdX(si, f0);
  MICROBOT_1_derivatives();

  /* f1 = f(t + (h/2), y + (h/2)*f0) */
  temp = 0.5 * h;
  for (i = 0; i < nXc; i++) {
    x[i] = y[i] + (temp*f0[i]);
  }

  rtsiSetT(si, t + temp);
  rtsiSetdX(si, f1);
  MICROBOT_1_step();
  MICROBOT_1_derivatives();

  /* f2 = f(t + (h/2), y + (h/2)*f1) */
  for (i = 0; i < nXc; i++) {
    x[i] = y[i] + (temp*f1[i]);
  }

  rtsiSetdX(si, f2);
  MICROBOT_1_step();
  MICROBOT_1_derivatives();

  /* f3 = f(t + h, y + h*f2) */
  for (i = 0; i < nXc; i++) {
    x[i] = y[i] + (h*f2[i]);
  }

  rtsiSetT(si, tnew);
  rtsiSetdX(si, f3);
  MICROBOT_1_step();
  MICROBOT_1_derivatives();

  /* tnew = t + h
     ynew = y + (h/6)*(f0 + 2*f1 + 2*f2 + 2*f3) */
  temp = h / 6.0;
  for (i = 0; i < nXc; i++) {
    x[i] = y[i] + temp*(f0[i] + 2.0*f1[i] + 2.0*f2[i] + f3[i]);
  }

  MICROBOT_1_step();
  MICROBOT_1_projection();
  rtsiSetSimTimeStep(si,MAJOR_TIME_STEP);
}

/* Model step function */
void MICROBOT_1_step(void)
{
  if (rtmIsMajorTimeStep(MICROBOT_1_M)) {
    /* set solver stop time */
    if (!(MICROBOT_1_M->Timing.clockTick0+1)) {
      rtsiSetSolverStopTime(&MICROBOT_1_M->solverInfo,
                            ((MICROBOT_1_M->Timing.clockTickH0 + 1) *
        MICROBOT_1_M->Timing.stepSize0 * 4294967296.0));
    } else {
      rtsiSetSolverStopTime(&MICROBOT_1_M->solverInfo,
                            ((MICROBOT_1_M->Timing.clockTick0 + 1) *
        MICROBOT_1_M->Timing.stepSize0 + MICROBOT_1_M->Timing.clockTickH0 *
        MICROBOT_1_M->Timing.stepSize0 * 4294967296.0));
    }
  }                                    /* end MajorTimeStep */

  /* Update absolute time of base rate at minor time step */
  if (rtmIsMinorTimeStep(MICROBOT_1_M)) {
    MICROBOT_1_M->Timing.t[0] = rtsiGetT(&MICROBOT_1_M->solverInfo);
  }

  if (rtmIsMajorTimeStep(MICROBOT_1_M)) {
    /* Gain: '<S15>/Slider Gain' incorporates:
     *  Constant: '<Root>/Constant1'
     */
    MICROBOT_1_B.SliderGain = MICROBOT_1_P.SliderGain6_gain *
      MICROBOT_1_P.Constant1_Value;

    /* Gain: '<Root>/Gain' */
    MICROBOT_1_B.Gain = MICROBOT_1_P.Gain_Gain * MICROBOT_1_B.SliderGain;

    /* Gain: '<S11>/Slider Gain' incorporates:
     *  Constant: '<Root>/Constant2'
     */
    MICROBOT_1_B.SliderGain_m = MICROBOT_1_P.SliderGain2_gain *
      MICROBOT_1_P.Constant2_Value;

    /* Gain: '<S12>/Slider Gain' incorporates:
     *  Constant: '<Root>/Constant3'
     */
    MICROBOT_1_B.SliderGain_k = MICROBOT_1_P.SliderGain3_gain *
      MICROBOT_1_P.Constant3_Value;

    /* Gain: '<S13>/Slider Gain' incorporates:
     *  Constant: '<Root>/Constant4'
     */
    MICROBOT_1_B.SliderGain_p = MICROBOT_1_P.SliderGain4_gain *
      MICROBOT_1_P.Constant4_Value;

    /* Gain: '<S14>/Slider Gain' incorporates:
     *  Constant: '<Root>/Constant5'
     */
    MICROBOT_1_B.SliderGain_i = MICROBOT_1_P.SliderGain5_gain *
      MICROBOT_1_P.Constant5_Value;
  }

  /* S-Function Block: <S16>/Block#1 */
  {
    _rtMech_PWORK *mechWork = (_rtMech_PWORK *) MICROBOT_1_DW.Block1_PWORK;
    mechWork->genSimData.time = MICROBOT_1_M->Timing.t[0];
    mechWork->outSimData.majorTimestep = rtmIsMajorTimeStep(MICROBOT_1_M);
    if (kinematicSfcnOutputMethod(mechWork->mechanism, &(mechWork->genSimData),
         &(mechWork->outSimData))) {
      {
        const ErrorRecord *err = mech_getErrorMsg();
        static char_T errorMsg[1024];
        sprintf(errorMsg,
                err->errorMsg,
                err->blocks[0],
                err->blocks[1],
                err->blocks[2],
                err->blocks[3],
                err->blocks[4]);
        rtmSetErrorStatus(MICROBOT_1_M, errorMsg);
        return;
      }
    }
  }

  if (rtmIsMajorTimeStep(MICROBOT_1_M)) {
    /* Gain: '<S16>/_gravity_conversion' incorporates:
     *  Constant: '<S9>/SOURCE_BLOCK'
     */
    MICROBOT_1_B._gravity_conversion[0] = MICROBOT_1_P._gravity_conversion_Gain *
      MICROBOT_1_P.MachineEnvironment_Gravity[0];
    MICROBOT_1_B._gravity_conversion[1] = MICROBOT_1_P._gravity_conversion_Gain *
      MICROBOT_1_P.MachineEnvironment_Gravity[1];
    MICROBOT_1_B._gravity_conversion[2] = MICROBOT_1_P._gravity_conversion_Gain *
      MICROBOT_1_P.MachineEnvironment_Gravity[2];
  }

  /* S-Function Block: <S16>/Block#2 */
  {
    _rtMech_PWORK *mechWork = (_rtMech_PWORK *) MICROBOT_1_DW.Block2_PWORK;
    mechWork->genSimData.time = MICROBOT_1_M->Timing.t[0];
    mechWork->outSimData.majorTimestep = rtmIsMajorTimeStep(MICROBOT_1_M);
    if (dynamicSfcnOutputMethod(mechWork->mechanism, &(mechWork->genSimData),
         &(mechWork->outSimData))) {
      {
        const ErrorRecord *err = mech_getErrorMsg();
        static char_T errorMsg[1024];
        sprintf(errorMsg,
                err->errorMsg,
                err->blocks[0],
                err->blocks[1],
                err->blocks[2],
                err->blocks[3],
                err->blocks[4]);
        rtmSetErrorStatus(MICROBOT_1_M, errorMsg);
        return;
      }
    }
  }

  /* S-Function Block: <S16>/Block#3 */
  {
    _rtMech_PWORK *mechWork = (_rtMech_PWORK *) MICROBOT_1_DW.Block3_PWORK;
    mechWork->genSimData.time = MICROBOT_1_M->Timing.t[0];
    mechWork->outSimData.majorTimestep = rtmIsMajorTimeStep(MICROBOT_1_M);
    if (eventSfcnOutputMethod(mechWork->mechanism, &(mechWork->genSimData),
         &(mechWork->outSimData))) {
      {
        const ErrorRecord *err = mech_getErrorMsg();
        static char_T errorMsg[1024];
        sprintf(errorMsg,
                err->errorMsg,
                err->blocks[0],
                err->blocks[1],
                err->blocks[2],
                err->blocks[3],
                err->blocks[4]);
        rtmSetErrorStatus(MICROBOT_1_M, errorMsg);
        return;
      }
    }
  }

  if (rtmIsMajorTimeStep(MICROBOT_1_M)) {
    /* Matfile logging */
    rt_UpdateTXYLogVars(MICROBOT_1_M->rtwLogInfo, (MICROBOT_1_M->Timing.t));
  }                                    /* end MajorTimeStep */

  if (rtmIsMajorTimeStep(MICROBOT_1_M)) {
    /* signal main to stop simulation */
    {                                  /* Sample time: [0.0s, 0.0s] */
      if ((rtmGetTFinal(MICROBOT_1_M)!=-1) &&
          !((rtmGetTFinal(MICROBOT_1_M)-(((MICROBOT_1_M->Timing.clockTick1+
               MICROBOT_1_M->Timing.clockTickH1* 4294967296.0)) * 0.001)) >
            (((MICROBOT_1_M->Timing.clockTick1+MICROBOT_1_M->Timing.clockTickH1*
               4294967296.0)) * 0.001) * (DBL_EPSILON))) {
        rtmSetErrorStatus(MICROBOT_1_M, "Simulation finished");
      }
    }

    rt_ertODEUpdateContinuousStates(&MICROBOT_1_M->solverInfo);

    /* Update absolute time for base rate */
    /* The "clockTick0" counts the number of times the code of this task has
     * been executed. The absolute time is the multiplication of "clockTick0"
     * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
     * overflow during the application lifespan selected.
     * Timer of this task consists of two 32 bit unsigned integers.
     * The two integers represent the low bits Timing.clockTick0 and the high bits
     * Timing.clockTickH0. When the low bit overflows to 0, the high bits increment.
     */
    if (!(++MICROBOT_1_M->Timing.clockTick0)) {
      ++MICROBOT_1_M->Timing.clockTickH0;
    }

    MICROBOT_1_M->Timing.t[0] = rtsiGetSolverStopTime(&MICROBOT_1_M->solverInfo);

    {
      /* Update absolute timer for sample time: [0.001s, 0.0s] */
      /* The "clockTick1" counts the number of times the code of this task has
       * been executed. The resolution of this integer timer is 0.001, which is the step size
       * of the task. Size of "clockTick1" ensures timer will not overflow during the
       * application lifespan selected.
       * Timer of this task consists of two 32 bit unsigned integers.
       * The two integers represent the low bits Timing.clockTick1 and the high bits
       * Timing.clockTickH1. When the low bit overflows to 0, the high bits increment.
       */
      MICROBOT_1_M->Timing.clockTick1++;
      if (!MICROBOT_1_M->Timing.clockTick1) {
        MICROBOT_1_M->Timing.clockTickH1++;
      }
    }
  }                                    /* end MajorTimeStep */
}

/* Derivatives for root system: '<Root>' */
void MICROBOT_1_derivatives(void)
{
  /* S-Function Block: <S16>/Block#1 */
  {
    _rtMech_PWORK *mechWork = (_rtMech_PWORK *) MICROBOT_1_DW.Block1_PWORK;
    if (sFcnDerivativesMethod(mechWork->mechanism, &((XDot_MICROBOT_1_T *)
          MICROBOT_1_M->ModelData.derivs)->Revolute9R1Position[0])) {
      {
        const ErrorRecord *err = mech_getErrorMsg();
        static char_T errorMsg[1024];
        sprintf(errorMsg,
                err->errorMsg,
                err->blocks[0],
                err->blocks[1],
                err->blocks[2],
                err->blocks[3],
                err->blocks[4]);
        rtmSetErrorStatus(MICROBOT_1_M, errorMsg);
        return;
      }
    }
  }
}

/* Model initialize function */
void MICROBOT_1_initialize(void)
{
  /* Registration code */

  /* initialize non-finites */
  rt_InitInfAndNaN(sizeof(real_T));

  /* initialize real-time model */
  (void) memset((void *)MICROBOT_1_M, 0,
                sizeof(RT_MODEL_MICROBOT_1_T));

  {
    /* Setup solver object */
    rtsiSetSimTimeStepPtr(&MICROBOT_1_M->solverInfo,
                          &MICROBOT_1_M->Timing.simTimeStep);
    rtsiSetTPtr(&MICROBOT_1_M->solverInfo, &rtmGetTPtr(MICROBOT_1_M));
    rtsiSetStepSizePtr(&MICROBOT_1_M->solverInfo,
                       &MICROBOT_1_M->Timing.stepSize0);
    rtsiSetdXPtr(&MICROBOT_1_M->solverInfo, &MICROBOT_1_M->ModelData.derivs);
    rtsiSetContStatesPtr(&MICROBOT_1_M->solverInfo, (real_T **)
                         &MICROBOT_1_M->ModelData.contStates);
    rtsiSetNumContStatesPtr(&MICROBOT_1_M->solverInfo,
      &MICROBOT_1_M->Sizes.numContStates);
    rtsiSetErrorStatusPtr(&MICROBOT_1_M->solverInfo, (&rtmGetErrorStatus
      (MICROBOT_1_M)));
    rtsiSetRTModelPtr(&MICROBOT_1_M->solverInfo, MICROBOT_1_M);
  }

  rtsiSetSimTimeStep(&MICROBOT_1_M->solverInfo, MAJOR_TIME_STEP);
  MICROBOT_1_M->ModelData.intgData.y = MICROBOT_1_M->ModelData.odeY;
  MICROBOT_1_M->ModelData.intgData.f[0] = MICROBOT_1_M->ModelData.odeF[0];
  MICROBOT_1_M->ModelData.intgData.f[1] = MICROBOT_1_M->ModelData.odeF[1];
  MICROBOT_1_M->ModelData.intgData.f[2] = MICROBOT_1_M->ModelData.odeF[2];
  MICROBOT_1_M->ModelData.intgData.f[3] = MICROBOT_1_M->ModelData.odeF[3];
  MICROBOT_1_M->ModelData.contStates = ((X_MICROBOT_1_T *) &MICROBOT_1_X);
  rtsiSetSolverData(&MICROBOT_1_M->solverInfo, (void *)
                    &MICROBOT_1_M->ModelData.intgData);
  rtsiSetSolverName(&MICROBOT_1_M->solverInfo,"ode4");
  rtmSetTPtr(MICROBOT_1_M, &MICROBOT_1_M->Timing.tArray[0]);
  rtmSetTFinal(MICROBOT_1_M, -1);
  MICROBOT_1_M->Timing.stepSize0 = 0.001;
  rtmSetFirstInitCond(MICROBOT_1_M, 1);

  /* Setup for data logging */
  {
    static RTWLogInfo rt_DataLoggingInfo;
    MICROBOT_1_M->rtwLogInfo = &rt_DataLoggingInfo;
  }

  /* Setup for data logging */
  {
    rtliSetLogXSignalInfo(MICROBOT_1_M->rtwLogInfo, (NULL));
    rtliSetLogXSignalPtrs(MICROBOT_1_M->rtwLogInfo, (NULL));
    rtliSetLogT(MICROBOT_1_M->rtwLogInfo, "tout");
    rtliSetLogX(MICROBOT_1_M->rtwLogInfo, "");
    rtliSetLogXFinal(MICROBOT_1_M->rtwLogInfo, "");
    rtliSetLogVarNameModifier(MICROBOT_1_M->rtwLogInfo, "rt_");
    rtliSetLogFormat(MICROBOT_1_M->rtwLogInfo, 0);
    rtliSetLogMaxRows(MICROBOT_1_M->rtwLogInfo, 1000);
    rtliSetLogDecimation(MICROBOT_1_M->rtwLogInfo, 1);
    rtliSetLogY(MICROBOT_1_M->rtwLogInfo, "");
    rtliSetLogYSignalInfo(MICROBOT_1_M->rtwLogInfo, (NULL));
    rtliSetLogYSignalPtrs(MICROBOT_1_M->rtwLogInfo, (NULL));
  }

  /* block I/O */
  (void) memset(((void *) &MICROBOT_1_B), 0,
                sizeof(B_MICROBOT_1_T));

  /* states (continuous) */
  {
    (void) memset((void *)&MICROBOT_1_X, 0,
                  sizeof(X_MICROBOT_1_T));
  }

  /* states (dwork) */
  (void) memset((void *)&MICROBOT_1_DW, 0,
                sizeof(DW_MICROBOT_1_T));

  /* Matfile logging */
  rt_StartDataLoggingWithStartTime(MICROBOT_1_M->rtwLogInfo, 0.0, rtmGetTFinal
    (MICROBOT_1_M), MICROBOT_1_M->Timing.stepSize0, (&rtmGetErrorStatus
    (MICROBOT_1_M)));

  /* S-Function Block: <S16>/Block#1 */
  {
    static _rtMech_PWORK mechWork;
    static ErrorRecord errorRec;
    if (rtmIsFirstInitCond(MICROBOT_1_M)) {
      const int locationFlag = __LINE__;
      if (rt_mech_visited_loc_MICROBOT_1_e2dc272 == 0 ) {
        rt_mech_visited_loc_MICROBOT_1_e2dc272 = locationFlag;
      }

      if (rt_mech_visited_loc_MICROBOT_1_e2dc272 == locationFlag ) {
        if ((++rt_mech_visited_MICROBOT_1_e2dc272) != 1) {
          static const char reentranterrormsg[] =
            "Attempting to use multiple instances of SimMechanics generated code";
          rtmSetErrorStatus(MICROBOT_1_M, reentranterrormsg);
          return;
        }
      }

      mechWork.mechanism = rt_get_mechanism_MICROBOT_1_e2dc272();
      mechWork.mechanism->engineError = &errorRec;
      mechWork.mechanism->engineError->errorFlag = false;

      {
        static char errorMsg[1024];
        if ((mechWork.mechanism->mapRuntimeData)(mechWork.mechanism,
             MICROBOT_1_P.Block1_SimMechanicsRuntimeParam, errorMsg, sizeof
             (errorMsg) - 1)) {
          rtmSetErrorStatus(MICROBOT_1_M, errorMsg);
          return;
        }
      }

      {
        static mech_method_table_t _mech_method_table = {
          NULL
          , NULL
          , mech_4D_hd4qrPL7Sjk8iSRNEz2
          , mech_IxHKTsH_3pIVJVQPMS66M0
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_VjsWU80i3CnNFpKd3QUvl0
          , mech_2OwKONgOLwAyyyipB5Kw02
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_o4ps9YGKcTKEIjCN5BZxU0
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_YKJotW7SzX758__JcQMsX_
          , NULL
          , mech_MXziSeUri_rFdG_U5Sbe01
          , NULL
          , mech_lRGNRK2aQOW7iCbdwcbtq2
          , NULL
          , NULL
          , NULL
          , mech_wQs_VwPvxj0_r5qn0NT8K_
          , mech_pNrZ5zKMuYJ8M1uXfT9bF_
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_ERNgctXrt7ZpZk2zBv9BP2
          , NULL
          , mech_BXbhsi8RpcFbkUD3ygZ5B0
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_NlW3W8O1U24dM9FXHRAUk1
          , NULL
          , mech_UcV4U23kZKFchc8F8Gv_d_
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_R1Wlp43Vyy28J2Zkhst08_
          , mech_Qu75Z7wvpnh4jASPIdYh_0
          , NULL
          , NULL
          , mech_HEVMRXG2twMdYXOl4FLye0
          , mech_YmWJ7IX2WWa6TdimqOD8D_
          , mech_oivmzI0CC_vAIrIulEloQ2
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_Sbc53fmaTgSa0tY0fkRZC2
          , NULL
          , mech_TBQ5BRA5xynf3KuBnwO1Z2
          , mech__R397Y1_xdNYhGBobYiYK0
          , mech_uqjEyqEaf2rgtG0X9VHzb0
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_tpSQGRBVQv4uWsI03XCq22
          , mech_ydoVMuYWgp5FoNEJvVzTB1
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_UBZmmgV6B4ZQXzGmko3tj0
          , mech_RgqwX6gnt92Bg6g_HIWj81
          , mech_XIcxt_pzz7lcfW6G9VAfI_
          , mech_9DTuq5G_tIDlG8swymAx91
          , mech_tLwU1ntiirHcHza4i_C_m_
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_svNiIcvnIGQmKB64tkbET0
          , mech_3nPr_4fUI_g4kWhIdFJf22
          , mech_3_72RQ_iqjKfiXmm0odAg2
          , NULL
          , mech_e97IG6Y1s4ZpZB3ichPZT0
          , NULL
          , NULL
          , NULL
          , mech_teSrDZKF_vEClhgAhg1ci1
          , NULL
          , mech_Lwd49CbzwasM6OSycFC871
          , mech_fjI5p0RcB0XgZi36eGpe40
          , mech_P2fVxNC2MyQ0D9T47XOdC2
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_1AypqhINVjYrduQeXY4HM_
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_ehYBPpWfOVRrYSplojAHb_
          , mech_W_ID0a35gI3U4I61wzEOC2
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_g40Gy75QmPkPrEdU1hX1c2
          , mech_QGHADAJiTcEcvMobImVQW_
          , mech_brQztLsR0_b9_9cG6d_yS0
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_AHMhfhIfpDYzSTBw8PIWf2
          , mech_IQnmXqndQ6caX61yQ4OCj2
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_TSfLI4eF5p0B_iB0wawgo2
          , NULL
          , NULL
          , NULL
          , mech_bQoFbl_taz1yD9aXn04Lp1
          , mech_6Knm8M49tgGx6hyp6eJCw0
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_KR9ZCK9E9tZi2A_zQBAmn0
          , mech_ues0XD4dVyon5_r2Jd3zo1
          , NULL
          , NULL
          , NULL
          , mech_xCsA1hGpENUD9DFN7m7UQ2
          , NULL
          , mech_pVENqzzNinHXVhmX8RjRZ0
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_1x_QYjXsuukSkiMv8gXnh0
          , NULL
          , NULL
          , NULL
          , NULL
          , mech__ZZij2Dcmvw4pXAD4tyY10
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_JA5E7EwbV4h_k868ZhJy_2
          , NULL
          , NULL
          , NULL
          , mech_rOIJlckzdxIPVOuU6j93f_
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_Z2tvyOygCA4tMPVQxpMRh2
          , NULL
          , mech_D96Fb1SmN8vJS_cwi_i_x_
          , NULL
          , mech_FyogrBtQY33kQFsvJ3dNM0
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_KFJbeY1D52GZQTkTwKTnh0
          , NULL
          , mech_qGIpOqVOTMA03eeQGq6x52
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_IOX2_Jd_Hh0qK7I7xFW9v2
          , mech_REZuEgKW3ConSwqvcM0TP1
          , mech_aszNzOaburh1GyUiG22P_1
          , mech_CeA2NooSCgAz_WlsXfSU12
          , mech_6ktggBz9P2W7CVGmfxpGX0
          , mech_z4Igm1JOCOaPcHmRW07PL2
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_Avmu1IlflobVWvWG6Ij_g_
          , mech_8Swa0cOlqYo8PhHugn4Ng_
          , mech_5NKPhliA8NsD4UI2qF1AG2
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_ToU5GXh5seUKuOfkmiKwE2
          , mech_7nKu2gTp34vLyKlk2hWSL_
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_iYPwGJK_PhWy2xyn6NVdK_
          , NULL
          , mech_tBE1oDp77LxkhtDlelp3H_
          , mech_G_m861Dk4ux3Qe2q_uZ8k1
          , mech_EJY9T8gkfG5eKoa4s5Re51
          , mech_8bofdWoolT_dVFkf1em6v0
          , mech_IvCSlQvvceAk2kiImsM6h0
          , mech_n1ygnHnG_GOZlhmJWLS1g1
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech__dBlukvsVsPdl6kExo1xR_
          , NULL
          , mech_kFFFaREX0BK4tp6FDgVUM1
          , NULL
          , mech_v6HJKeOBtLTTs6NoPsvJp1
          , NULL
          , mech_k5yUZgN53kEOG0IAk2P5o_
          , NULL
          , mech_RI5syhsMO6u5WNeXsGSUb_
          , NULL
          , mech_2kWqPiXFixaE_7H0tQFsb2
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_YxxbiR8LURz1uX3U07aPd1
          , NULL
          , mech_6iKWs5EnCFige2s2CNToQ_
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_96Uqbmeo_bmDtTSuPHzWP0
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_ywRB74_K3k__b5BBYw30C2
          , NULL
          , mech_jE7JEU9gcLQyG4heZr3cQ1
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech__QcbzHVelpSvM3h6Lcogn2
          , NULL
          , NULL
          , mech_zJ78UKtCP0HXHeMWjwAsR0
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_3RwHS4kcX6dUiTOqb52i8_
          , mech_qBOb0mwznlf1OfxAhv_WU2
          , NULL
          , NULL
          , mech_hZFLP8jeqGyb71nRA4mme1
          , NULL
          , mech_pIcZ4W23f1E_hfSl6nEl31
          , NULL
          , NULL
          , mech_H4eEYk_myuS9e8Lyx8qQX1
          , NULL
          , mech_XpyBK8DE5S0VbNRvncbOT_
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , mech_aVLYoA_8CmYQ_LAQb0BFV_
          , mech_xrRgsldxl5LYxJva1JePp1
          , NULL
          , mech_TKZbILt1lPf6_e4gTfMTA_
          , NULL
          , mech_h4anTbE0Se__gDUgjpRP_0
          , NULL
          , mech_3HJFfcbrhh9FwdxUMJoAE0
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
          , NULL
        };

        mech_method_table_update(&_mech_method_table);
      }

      if (createEngineMechanism(mechWork.mechanism)) {
        {
          const ErrorRecord *err = mech_getErrorMsg();
          static char_T errorMsg[1024];
          sprintf(errorMsg,
                  err->errorMsg,
                  err->blocks[0],
                  err->blocks[1],
                  err->blocks[2],
                  err->blocks[3],
                  err->blocks[4]);
          rtmSetErrorStatus(MICROBOT_1_M, errorMsg);
          return;
        }
      }

      mechWork.mechanism->state = &MICROBOT_1_X.Revolute9R1Position[0];
      MICROBOT_1_DW.Block1_IWORK = 0U;
      mechWork.genSimData.tStart = (0.0);
      mechWork.genSimData.iwork = &MICROBOT_1_DW.Block1_IWORK;
      mechWork.genSimData.numInputPorts = 2;

      {
        static real_T *mech_inputSignals[21];
        mech_inputSignals[0] = (real_T *) &MICROBOT_1_B.SliderGain;
        mech_inputSignals[1] = (real_T *) &MICROBOT_1_P.Constant19_Value;
        mech_inputSignals[2] = (real_T *) &MICROBOT_1_P.Constant20_Value;
        mech_inputSignals[3] = (real_T *) &MICROBOT_1_B.Gain;
        mech_inputSignals[4] = (real_T *) &MICROBOT_1_P.Constant17_Value;
        mech_inputSignals[5] = (real_T *) &MICROBOT_1_P.Constant18_Value;
        mech_inputSignals[6] = (real_T *) &MICROBOT_1_B.SliderGain_i;
        mech_inputSignals[7] = (real_T *) &MICROBOT_1_P.Constant15_Value;
        mech_inputSignals[8] = (real_T *) &MICROBOT_1_P.Constant16_Value;
        mech_inputSignals[9] = (real_T *) &MICROBOT_1_B.SliderGain_p;
        mech_inputSignals[10] = (real_T *) &MICROBOT_1_P.Constant13_Value;
        mech_inputSignals[11] = (real_T *) &MICROBOT_1_P.Constant14_Value;
        mech_inputSignals[12] = (real_T *) &MICROBOT_1_B.SliderGain_k;
        mech_inputSignals[13] = (real_T *) &MICROBOT_1_P.Constant11_Value;
        mech_inputSignals[14] = (real_T *) &MICROBOT_1_P.Constant12_Value;
        mech_inputSignals[15] = (real_T *) &MICROBOT_1_B.SliderGain_m;
        mech_inputSignals[16] = (real_T *) &MICROBOT_1_P.Constant9_Value;
        mech_inputSignals[17] = (real_T *) &MICROBOT_1_P.Constant10_Value;
        mech_inputSignals[18] = (real_T *) &MICROBOT_1_P.Constant_Value;
        mech_inputSignals[19] = (real_T *) &MICROBOT_1_P.Constant7_Value;
        mech_inputSignals[20] = (real_T *) &MICROBOT_1_P.Constant8_Value;
        mechWork.genSimData.inputSignals[0] = mech_inputSignals;
      }

      {
        static real_T *mech_inputSignals[3];
        mech_inputSignals[0] = (real_T *) &MICROBOT_1_B._gravity_conversion[0];
        mech_inputSignals[1] = (real_T *) &MICROBOT_1_B._gravity_conversion[1];
        mech_inputSignals[2] = (real_T *) &MICROBOT_1_B._gravity_conversion[2];
        mechWork.genSimData.inputSignals[1] = mech_inputSignals;
      }

      mechWork.outSimData.numOutputPorts = 2;
      mechWork.outSimData.logOutput = false;
      mechWork.outSimData.outputSignals[0] = &MICROBOT_1_B.Block1_o1[0];
      mechWork.outSimData.outputSignals[1] = &MICROBOT_1_B.Block1_o2;
      MICROBOT_1_DW.Block1_PWORK = &mechWork;
    }
  }

  /* S-Function Block: <S16>/Block#2 */
  {
    static _rtMech_PWORK mechWork;
    static ErrorRecord errorRec;
    if (rtmIsFirstInitCond(MICROBOT_1_M)) {
      mechWork.mechanism = rt_get_mechanism_MICROBOT_1_e2dc272();
      mechWork.mechanism->engineError = &errorRec;
      mechWork.mechanism->engineError->errorFlag = false;
      mechWork.genSimData.tStart = (0.0);
      mechWork.genSimData.iwork = NULL;
      mechWork.genSimData.numInputPorts = 3;

      {
        static real_T *mech_inputSignals[8];
        mech_inputSignals[0] = (real_T *) &MICROBOT_1_B.Block1_o1[0];
        mech_inputSignals[1] = (real_T *) &MICROBOT_1_B.Block1_o1[1];
        mech_inputSignals[2] = (real_T *) &MICROBOT_1_B.Block1_o1[2];
        mech_inputSignals[3] = (real_T *) &MICROBOT_1_B.Block1_o1[3];
        mech_inputSignals[4] = (real_T *) &MICROBOT_1_B.Block1_o1[4];
        mech_inputSignals[5] = (real_T *) &MICROBOT_1_B.Block1_o1[5];
        mech_inputSignals[6] = (real_T *) &MICROBOT_1_B.Block1_o1[6];
        mech_inputSignals[7] = (real_T *) &MICROBOT_1_B.Block1_o1[7];
        mechWork.genSimData.inputSignals[0] = mech_inputSignals;
      }

      {
        static real_T *mech_inputSignals[1];
        mech_inputSignals[0] = (real_T *) &MICROBOT_1_B.Block1_o2;
        mechWork.genSimData.inputSignals[1] = mech_inputSignals;
      }

      {
        static real_T *mech_inputSignals[3];
        mech_inputSignals[0] = (real_T *) &MICROBOT_1_B._gravity_conversion[0];
        mech_inputSignals[1] = (real_T *) &MICROBOT_1_B._gravity_conversion[1];
        mech_inputSignals[2] = (real_T *) &MICROBOT_1_B._gravity_conversion[2];
        mechWork.genSimData.inputSignals[2] = mech_inputSignals;
      }

      mechWork.outSimData.numOutputPorts = 1;
      mechWork.outSimData.logOutput = false;
      mechWork.outSimData.outputSignals[0] = &MICROBOT_1_B.Block2;
      MICROBOT_1_DW.Block2_PWORK = &mechWork;
    }
  }

  /* S-Function Block: <S16>/Block#3 */
  {
    static _rtMech_PWORK mechWork;
    static ErrorRecord errorRec;
    if (rtmIsFirstInitCond(MICROBOT_1_M)) {
      mechWork.mechanism = rt_get_mechanism_MICROBOT_1_e2dc272();
      mechWork.mechanism->engineError = &errorRec;
      mechWork.mechanism->engineError->errorFlag = false;
      MICROBOT_1_DW.Block3_IWORK = 1U;
      mechWork.genSimData.tStart = (0.0);
      mechWork.genSimData.iwork = &MICROBOT_1_DW.Block3_IWORK;
      mechWork.genSimData.numInputPorts = 1;

      {
        static real_T *mech_inputSignals[1];
        mech_inputSignals[0] = (real_T *) &MICROBOT_1_B.Block2;
        mechWork.genSimData.inputSignals[0] = mech_inputSignals;
      }

      mechWork.outSimData.numOutputPorts = 1;
      mechWork.outSimData.logOutput = false;
      mechWork.outSimData.outputSignals[0] = &MICROBOT_1_B.Block3;
      MICROBOT_1_DW.Block3_PWORK = &mechWork;
    }
  }

  /* set "at time zero" to false */
  if (rtmIsFirstInitCond(MICROBOT_1_M)) {
    rtmSetFirstInitCond(MICROBOT_1_M, 0);
  }
}

/* Model terminate function */
void MICROBOT_1_terminate(void)
{
  /* S-Function Block: <S16>/Block#1 */
  {
    if (rt_mech_visited_MICROBOT_1_e2dc272 == 1) {
      _rtMech_PWORK *mechWork = (_rtMech_PWORK *) MICROBOT_1_DW.Block1_PWORK;
      if (mechWork->mechanism->destroyEngine != NULL) {
        (mechWork->mechanism->destroyEngine)(mechWork->mechanism);
      }
    }

    if ((--rt_mech_visited_MICROBOT_1_e2dc272) == 0 ) {
      rt_mech_visited_loc_MICROBOT_1_e2dc272 = 0;
    }
  }
}
