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
boolean_T rt_map_mechanism_params_MICROBOT_1_e2dc272(Mechanism * mechanism, const real_T * input, char_T * msg, uint32_T msg_size)
{
    static real_T work[3465];
    real_T *output = 0;
    boolean_T error = 0;
    output = mechanism->runtimeData;
    memset(work, 0, sizeof(work));
    work[0] = 1.0;
    work[7] = 1.0;
    work[8] = 1.0;
    work[12] = 1.0;
    work[16] = 1.0;
    work[2929] = 1.0;
    work[2933] = 1.0;
    work[2937] = 1.0;
    work[2960] = 1.0;
    work[2964] = 1.0;
    work[2968] = 1.0;
    work[2991] = 1.0;
    work[2995] = 1.0;
    work[2999] = 1.0;
    work[3022] = 1.0;
    work[3026] = 1.0;
    work[3030] = 1.0;
    work[3053] = 1.0;
    work[3057] = 1.0;
    work[3061] = 1.0;
    work[3084] = 1.0;
    work[3088] = 1.0;
    work[3092] = 1.0;
    work[3115] = 1.0;
    work[3119] = 1.0;
    work[3123] = 1.0;
    work[3146] = 1.0;
    work[3150] = 1.0;
    work[3154] = 1.0;
    work[3177] = 1.0;
    work[3181] = 1.0;
    work[3185] = 1.0;
    work[3208] = 1.0;
    work[3212] = 1.0;
    work[3216] = 1.0;
    work[3239] = 1.0;
    work[3243] = 1.0;
    work[3247] = 1.0;
    work[3270] = 1.0;
    work[3274] = 1.0;
    work[3278] = 1.0;
    work[3301] = 1.0;
    work[3305] = 1.0;
    work[3309] = 1.0;
    work[3332] = 1.0;
    work[3336] = 1.0;
    work[3340] = 1.0;
    work[3456] = 1.0;
    work[3460] = 1.0;
    work[3464] = 1.0;
    pmVectorFunction((work + 17), (input + 560), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 20), (input + 563), (9 * sizeof(double)));
    work[29] = pmDet3by3((work + 20));
    pmVectorFunction((work + 30), work, (work + 29), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[30] = fabs(work[30]);
    if (work[30] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-11: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 31), (work + 20), (work + 20), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 40), (work + 8), (work + 31), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 49), (work + 40), (work + 40), 9, 1, 9, 1, 1, 1, 3);
    work[49] = sqrt(work[49]);
    work[49] = fabs(work[49]);
    if (work[49] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-11: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 20), (work + 50));
    pmVectorFunction((work + 59), (input + 582), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 62), (input + 585), (9 * sizeof(double)));
    work[71] = pmDet3by3((work + 62));
    pmVectorFunction((work + 72), work, (work + 71), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[72] = fabs(work[72]);
    if (work[72] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-11: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 73), (work + 62), (work + 62), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 82), (work + 8), (work + 73), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 91), (work + 82), (work + 82), 9, 1, 9, 1, 1, 1, 3);
    work[91] = sqrt(work[91]);
    work[91] = fabs(work[91]);
    if (work[91] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-11: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 62), (work + 92));
    pmVectorFunction((work + 101), (input + 594), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 104), (input + 597), (9 * sizeof(double)));
    work[113] = pmDet3by3((work + 104));
    pmVectorFunction((work + 114), work, (work + 113), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[114] = fabs(work[114]);
    if (work[114] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-11: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 115), (work + 104), (work + 104), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 124), (work + 8), (work + 115), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 133), (work + 124), (work + 124), 9, 1, 9, 1, 1, 1, 3);
    work[133] = sqrt(work[133]);
    work[133] = fabs(work[133]);
    if (work[133] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-11: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 104), (work + 134));
    pmVectorFunction((work + 143), (input + 606), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 146), (input + 609), (9 * sizeof(double)));
    work[155] = pmDet3by3((work + 146));
    pmVectorFunction((work + 156), work, (work + 155), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[156] = fabs(work[156]);
    if (work[156] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-11: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 157), (work + 146), (work + 146), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 166), (work + 8), (work + 157), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 175), (work + 166), (work + 166), 9, 1, 9, 1, 1, 1, 3);
    work[175] = sqrt(work[175]);
    work[175] = fabs(work[175]);
    if (work[175] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-11: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 146), (work + 176));
    pmVectorFunction((work + 185), (input + 581), (work + 1), 0.0, 1.0, 0.0, 1, 1, 1, 0);
    pmVectorFunction((work + 186), (input + 572), (work + 1), 0.0, 1.0, 0.0, 9, 1, 1, 0);
    memcpy((work + 195), (work + 186), (9 * sizeof(double)));
    pmVectorFunction((work + 204), (input + 792), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 207), (input + 795), (9 * sizeof(double)));
    work[216] = pmDet3by3((work + 207));
    pmVectorFunction((work + 217), work, (work + 216), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[217] = fabs(work[217]);
    if (work[217] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W08-6: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 218), (work + 207), (work + 207), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 227), (work + 8), (work + 218), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 236), (work + 227), (work + 227), 9, 1, 9, 1, 1, 1, 3);
    work[236] = sqrt(work[236]);
    work[236] = fabs(work[236]);
    if (work[236] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W08-6: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 207), (work + 237));
    pmVectorFunction((work + 246), (input + 814), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 249), (input + 817), (9 * sizeof(double)));
    work[258] = pmDet3by3((work + 249));
    pmVectorFunction((work + 259), work, (work + 258), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[259] = fabs(work[259]);
    if (work[259] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W08-6: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 260), (work + 249), (work + 249), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 269), (work + 8), (work + 260), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 278), (work + 269), (work + 269), 9, 1, 9, 1, 1, 1, 3);
    work[278] = sqrt(work[278]);
    work[278] = fabs(work[278]);
    if (work[278] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W08-6: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 249), (work + 279));
    pmVectorFunction((work + 288), (input + 826), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 291), (input + 829), (9 * sizeof(double)));
    work[300] = pmDet3by3((work + 291));
    pmVectorFunction((work + 301), work, (work + 300), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[301] = fabs(work[301]);
    if (work[301] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W08-6: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 302), (work + 291), (work + 291), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 311), (work + 8), (work + 302), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 320), (work + 311), (work + 311), 9, 1, 9, 1, 1, 1, 3);
    work[320] = sqrt(work[320]);
    work[320] = fabs(work[320]);
    if (work[320] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W08-6: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 291), (work + 321));
    pmVectorFunction((work + 330), (input + 838), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 333), (input + 841), (9 * sizeof(double)));
    work[342] = pmDet3by3((work + 333));
    pmVectorFunction((work + 343), work, (work + 342), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[343] = fabs(work[343]);
    if (work[343] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W08-6: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 344), (work + 333), (work + 333), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 353), (work + 8), (work + 344), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 362), (work + 353), (work + 353), 9, 1, 9, 1, 1, 1, 3);
    work[362] = sqrt(work[362]);
    work[362] = fabs(work[362]);
    if (work[362] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W08-6: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 333), (work + 363));
    pmVectorFunction((work + 372), (input + 813), (work + 1), 0.0, 1.0, 0.0, 1, 1, 1, 0);
    pmVectorFunction((work + 373), (input + 804), (work + 1), 0.0, 1.0, 0.0, 9, 1, 1, 0);
    memcpy((work + 382), (work + 373), (9 * sizeof(double)));
    pmVectorFunction((work + 391), (input + 618), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 394), (input + 621), (9 * sizeof(double)));
    work[403] = pmDet3by3((work + 394));
    pmVectorFunction((work + 404), work, (work + 403), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[404] = fabs(work[404]);
    if (work[404] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-12: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 405), (work + 394), (work + 394), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 414), (work + 8), (work + 405), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 423), (work + 414), (work + 414), 9, 1, 9, 1, 1, 1, 3);
    work[423] = sqrt(work[423]);
    work[423] = fabs(work[423]);
    if (work[423] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-12: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 394), (work + 424));
    pmVectorFunction((work + 433), (input + 640), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 436), (input + 643), (9 * sizeof(double)));
    work[445] = pmDet3by3((work + 436));
    pmVectorFunction((work + 446), work, (work + 445), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[446] = fabs(work[446]);
    if (work[446] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-12: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 447), (work + 436), (work + 436), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 456), (work + 8), (work + 447), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 465), (work + 456), (work + 456), 9, 1, 9, 1, 1, 1, 3);
    work[465] = sqrt(work[465]);
    work[465] = fabs(work[465]);
    if (work[465] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-12: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 436), (work + 466));
    pmVectorFunction((work + 475), (input + 652), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 478), (input + 655), (9 * sizeof(double)));
    work[487] = pmDet3by3((work + 478));
    pmVectorFunction((work + 488), work, (work + 487), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[488] = fabs(work[488]);
    if (work[488] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-12: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 489), (work + 478), (work + 478), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 498), (work + 8), (work + 489), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 507), (work + 498), (work + 498), 9, 1, 9, 1, 1, 1, 3);
    work[507] = sqrt(work[507]);
    work[507] = fabs(work[507]);
    if (work[507] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-12: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 478), (work + 508));
    pmVectorFunction((work + 517), (input + 664), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 520), (input + 667), (9 * sizeof(double)));
    work[529] = pmDet3by3((work + 520));
    pmVectorFunction((work + 530), work, (work + 529), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[530] = fabs(work[530]);
    if (work[530] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-12: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 531), (work + 520), (work + 520), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 540), (work + 8), (work + 531), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 549), (work + 540), (work + 540), 9, 1, 9, 1, 1, 1, 3);
    work[549] = sqrt(work[549]);
    work[549] = fabs(work[549]);
    if (work[549] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-12: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 520), (work + 550));
    pmVectorFunction((work + 559), (input + 639), (work + 1), 0.0, 1.0, 0.0, 1, 1, 1, 0);
    pmVectorFunction((work + 560), (input + 630), (work + 1), 0.0, 1.0, 0.0, 9, 1, 1, 0);
    memcpy((work + 569), (work + 560), (9 * sizeof(double)));
    pmVectorFunction((work + 578), (input + 676), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 581), (input + 679), (9 * sizeof(double)));
    work[590] = pmDet3by3((work + 581));
    pmVectorFunction((work + 591), work, (work + 590), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[591] = fabs(work[591]);
    if (work[591] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-9: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 592), (work + 581), (work + 581), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 601), (work + 8), (work + 592), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 610), (work + 601), (work + 601), 9, 1, 9, 1, 1, 1, 3);
    work[610] = sqrt(work[610]);
    work[610] = fabs(work[610]);
    if (work[610] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-9: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 581), (work + 611));
    pmVectorFunction((work + 620), (input + 698), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 623), (input + 701), (9 * sizeof(double)));
    work[632] = pmDet3by3((work + 623));
    pmVectorFunction((work + 633), work, (work + 632), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[633] = fabs(work[633]);
    if (work[633] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-9: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 634), (work + 623), (work + 623), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 643), (work + 8), (work + 634), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 652), (work + 643), (work + 643), 9, 1, 9, 1, 1, 1, 3);
    work[652] = sqrt(work[652]);
    work[652] = fabs(work[652]);
    if (work[652] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-9: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 623), (work + 653));
    pmVectorFunction((work + 662), (input + 710), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 665), (input + 713), (9 * sizeof(double)));
    work[674] = pmDet3by3((work + 665));
    pmVectorFunction((work + 675), work, (work + 674), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[675] = fabs(work[675]);
    if (work[675] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-9: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 676), (work + 665), (work + 665), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 685), (work + 8), (work + 676), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 694), (work + 685), (work + 685), 9, 1, 9, 1, 1, 1, 3);
    work[694] = sqrt(work[694]);
    work[694] = fabs(work[694]);
    if (work[694] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-9: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 665), (work + 695));
    pmVectorFunction((work + 704), (input + 722), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 707), (input + 725), (9 * sizeof(double)));
    work[716] = pmDet3by3((work + 707));
    pmVectorFunction((work + 717), work, (work + 716), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[717] = fabs(work[717]);
    if (work[717] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-9: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 718), (work + 707), (work + 707), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 727), (work + 8), (work + 718), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 736), (work + 727), (work + 727), 9, 1, 9, 1, 1, 1, 3);
    work[736] = sqrt(work[736]);
    work[736] = fabs(work[736]);
    if (work[736] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-9: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 707), (work + 737));
    pmVectorFunction((work + 746), (input + 697), (work + 1), 0.0, 1.0, 0.0, 1, 1, 1, 0);
    pmVectorFunction((work + 747), (input + 688), (work + 1), 0.0, 1.0, 0.0, 9, 1, 1, 0);
    memcpy((work + 756), (work + 747), (9 * sizeof(double)));
    pmVectorFunction((work + 765), (input + 734), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 768), (input + 737), (9 * sizeof(double)));
    work[777] = pmDet3by3((work + 768));
    pmVectorFunction((work + 778), work, (work + 777), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[778] = fabs(work[778]);
    if (work[778] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W08-5: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 779), (work + 768), (work + 768), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 788), (work + 8), (work + 779), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 797), (work + 788), (work + 788), 9, 1, 9, 1, 1, 1, 3);
    work[797] = sqrt(work[797]);
    work[797] = fabs(work[797]);
    if (work[797] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W08-5: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 768), (work + 798));
    pmVectorFunction((work + 807), (input + 756), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 810), (input + 759), (9 * sizeof(double)));
    work[819] = pmDet3by3((work + 810));
    pmVectorFunction((work + 820), work, (work + 819), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[820] = fabs(work[820]);
    if (work[820] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W08-5: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 821), (work + 810), (work + 810), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 830), (work + 8), (work + 821), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 839), (work + 830), (work + 830), 9, 1, 9, 1, 1, 1, 3);
    work[839] = sqrt(work[839]);
    work[839] = fabs(work[839]);
    if (work[839] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W08-5: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 810), (work + 840));
    pmVectorFunction((work + 849), (input + 768), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 852), (input + 771), (9 * sizeof(double)));
    work[861] = pmDet3by3((work + 852));
    pmVectorFunction((work + 862), work, (work + 861), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[862] = fabs(work[862]);
    if (work[862] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W08-5: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 863), (work + 852), (work + 852), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 872), (work + 8), (work + 863), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 881), (work + 872), (work + 872), 9, 1, 9, 1, 1, 1, 3);
    work[881] = sqrt(work[881]);
    work[881] = fabs(work[881]);
    if (work[881] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W08-5: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 852), (work + 882));
    pmVectorFunction((work + 891), (input + 780), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 894), (input + 783), (9 * sizeof(double)));
    work[903] = pmDet3by3((work + 894));
    pmVectorFunction((work + 904), work, (work + 903), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[904] = fabs(work[904]);
    if (work[904] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W08-5: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 905), (work + 894), (work + 894), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 914), (work + 8), (work + 905), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 923), (work + 914), (work + 914), 9, 1, 9, 1, 1, 1, 3);
    work[923] = sqrt(work[923]);
    work[923] = fabs(work[923]);
    if (work[923] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W08-5: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 894), (work + 924));
    pmVectorFunction((work + 933), (input + 755), (work + 1), 0.0, 1.0, 0.0, 1, 1, 1, 0);
    pmVectorFunction((work + 934), (input + 746), (work + 1), 0.0, 1.0, 0.0, 9, 1, 1, 0);
    memcpy((work + 943), (work + 934), (9 * sizeof(double)));
    pmVectorFunction((work + 952), (input + 502), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 955), (input + 505), (9 * sizeof(double)));
    work[964] = pmDet3by3((work + 955));
    pmVectorFunction((work + 965), work, (work + 964), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[965] = fabs(work[965]);
    if (work[965] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-10: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 966), (work + 955), (work + 955), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 975), (work + 8), (work + 966), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 984), (work + 975), (work + 975), 9, 1, 9, 1, 1, 1, 3);
    work[984] = sqrt(work[984]);
    work[984] = fabs(work[984]);
    if (work[984] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-10: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 955), (work + 985));
    pmVectorFunction((work + 994), (input + 524), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 997), (input + 527), (9 * sizeof(double)));
    work[1006] = pmDet3by3((work + 997));
    pmVectorFunction((work + 1007), work, (work + 1006), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1007] = fabs(work[1007]);
    if (work[1007] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-10: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1008), (work + 997), (work + 997), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1017), (work + 8), (work + 1008), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1026), (work + 1017), (work + 1017), 9, 1, 9, 1, 1, 1, 3);
    work[1026] = sqrt(work[1026]);
    work[1026] = fabs(work[1026]);
    if (work[1026] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-10: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 997), (work + 1027));
    pmVectorFunction((work + 1036), (input + 536), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1039), (input + 539), (9 * sizeof(double)));
    work[1048] = pmDet3by3((work + 1039));
    pmVectorFunction((work + 1049), work, (work + 1048), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1049] = fabs(work[1049]);
    if (work[1049] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-10: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1050), (work + 1039), (work + 1039), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1059), (work + 8), (work + 1050), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1068), (work + 1059), (work + 1059), 9, 1, 9, 1, 1, 1, 3);
    work[1068] = sqrt(work[1068]);
    work[1068] = fabs(work[1068]);
    if (work[1068] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-10: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1039), (work + 1069));
    pmVectorFunction((work + 1078), (input + 548), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1081), (input + 551), (9 * sizeof(double)));
    work[1090] = pmDet3by3((work + 1081));
    pmVectorFunction((work + 1091), work, (work + 1090), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1091] = fabs(work[1091]);
    if (work[1091] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-10: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1092), (work + 1081), (work + 1081), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1101), (work + 8), (work + 1092), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1110), (work + 1101), (work + 1101), 9, 1, 9, 1, 1, 1, 3);
    work[1110] = sqrt(work[1110]);
    work[1110] = fabs(work[1110]);
    if (work[1110] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W07-10: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1081), (work + 1111));
    pmVectorFunction((work + 1120), (input + 523), (work + 1), 0.0, 1.0, 0.0, 1, 1, 1, 0);
    pmVectorFunction((work + 1121), (input + 514), (work + 1), 0.0, 1.0, 0.0, 9, 1, 1, 0);
    memcpy((work + 1130), (work + 1121), (9 * sizeof(double)));
    pmVectorFunction((work + 1139), (input + 408), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1142), (input + 411), (9 * sizeof(double)));
    work[1151] = pmDet3by3((work + 1142));
    pmVectorFunction((work + 1152), work, (work + 1151), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1152] = fabs(work[1152]);
    if (work[1152] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W06-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1153), (work + 1142), (work + 1142), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1162), (work + 8), (work + 1153), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1171), (work + 1162), (work + 1162), 9, 1, 9, 1, 1, 1, 3);
    work[1171] = sqrt(work[1171]);
    work[1171] = fabs(work[1171]);
    if (work[1171] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W06-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1142), (work + 1172));
    pmVectorFunction((work + 1181), (input + 430), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1184), (input + 433), (9 * sizeof(double)));
    work[1193] = pmDet3by3((work + 1184));
    pmVectorFunction((work + 1194), work, (work + 1193), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1194] = fabs(work[1194]);
    if (work[1194] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W06-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1195), (work + 1184), (work + 1184), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1204), (work + 8), (work + 1195), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1213), (work + 1204), (work + 1204), 9, 1, 9, 1, 1, 1, 3);
    work[1213] = sqrt(work[1213]);
    work[1213] = fabs(work[1213]);
    if (work[1213] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W06-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1184), (work + 1214));
    pmVectorFunction((work + 1223), (input + 442), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1226), (input + 445), (9 * sizeof(double)));
    work[1235] = pmDet3by3((work + 1226));
    pmVectorFunction((work + 1236), work, (work + 1235), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1236] = fabs(work[1236]);
    if (work[1236] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W06-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1237), (work + 1226), (work + 1226), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1246), (work + 8), (work + 1237), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1255), (work + 1246), (work + 1246), 9, 1, 9, 1, 1, 1, 3);
    work[1255] = sqrt(work[1255]);
    work[1255] = fabs(work[1255]);
    if (work[1255] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W06-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1226), (work + 1256));
    pmVectorFunction((work + 1265), (input + 454), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1268), (input + 457), (9 * sizeof(double)));
    work[1277] = pmDet3by3((work + 1268));
    pmVectorFunction((work + 1278), work, (work + 1277), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1278] = fabs(work[1278]);
    if (work[1278] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W06-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1279), (work + 1268), (work + 1268), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1288), (work + 8), (work + 1279), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1297), (work + 1288), (work + 1288), 9, 1, 9, 1, 1, 1, 3);
    work[1297] = sqrt(work[1297]);
    work[1297] = fabs(work[1297]);
    if (work[1297] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W06-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1268), (work + 1298));
    pmVectorFunction((work + 1307), (input + 466), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1310), (input + 469), (9 * sizeof(double)));
    work[1319] = pmDet3by3((work + 1310));
    pmVectorFunction((work + 1320), work, (work + 1319), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1320] = fabs(work[1320]);
    if (work[1320] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W06-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1321), (work + 1310), (work + 1310), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1330), (work + 8), (work + 1321), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1339), (work + 1330), (work + 1330), 9, 1, 9, 1, 1, 1, 3);
    work[1339] = sqrt(work[1339]);
    work[1339] = fabs(work[1339]);
    if (work[1339] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W06-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1310), (work + 1340));
    pmVectorFunction((work + 1349), (input + 478), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1352), (input + 481), (9 * sizeof(double)));
    work[1361] = pmDet3by3((work + 1352));
    pmVectorFunction((work + 1362), work, (work + 1361), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1362] = fabs(work[1362]);
    if (work[1362] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W06-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1363), (work + 1352), (work + 1352), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1372), (work + 8), (work + 1363), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1381), (work + 1372), (work + 1372), 9, 1, 9, 1, 1, 1, 3);
    work[1381] = sqrt(work[1381]);
    work[1381] = fabs(work[1381]);
    if (work[1381] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W06-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1352), (work + 1382));
    pmVectorFunction((work + 1391), (input + 490), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1394), (input + 493), (9 * sizeof(double)));
    work[1403] = pmDet3by3((work + 1394));
    pmVectorFunction((work + 1404), work, (work + 1403), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1404] = fabs(work[1404]);
    if (work[1404] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W06-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1405), (work + 1394), (work + 1394), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1414), (work + 8), (work + 1405), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1423), (work + 1414), (work + 1414), 9, 1, 9, 1, 1, 1, 3);
    work[1423] = sqrt(work[1423]);
    work[1423] = fabs(work[1423]);
    if (work[1423] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W06-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1394), (work + 1424));
    pmVectorFunction((work + 1433), (input + 429), (work + 1), 0.0, 1.0, 0.0, 1, 1, 1, 0);
    pmVectorFunction((work + 1434), (input + 420), (work + 1), 0.0, 1.0, 0.0, 9, 1, 1, 0);
    memcpy((work + 1443), (work + 1434), (9 * sizeof(double)));
    pmVectorFunction((work + 1452), (input + 350), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1455), (input + 353), (9 * sizeof(double)));
    work[1464] = pmDet3by3((work + 1455));
    pmVectorFunction((work + 1465), work, (work + 1464), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1465] = fabs(work[1465]);
    if (work[1465] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W05-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1466), (work + 1455), (work + 1455), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1475), (work + 8), (work + 1466), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1484), (work + 1475), (work + 1475), 9, 1, 9, 1, 1, 1, 3);
    work[1484] = sqrt(work[1484]);
    work[1484] = fabs(work[1484]);
    if (work[1484] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W05-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1455), (work + 1485));
    pmVectorFunction((work + 1494), (input + 372), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1497), (input + 375), (9 * sizeof(double)));
    work[1506] = pmDet3by3((work + 1497));
    pmVectorFunction((work + 1507), work, (work + 1506), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1507] = fabs(work[1507]);
    if (work[1507] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W05-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1508), (work + 1497), (work + 1497), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1517), (work + 8), (work + 1508), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1526), (work + 1517), (work + 1517), 9, 1, 9, 1, 1, 1, 3);
    work[1526] = sqrt(work[1526]);
    work[1526] = fabs(work[1526]);
    if (work[1526] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W05-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1497), (work + 1527));
    pmVectorFunction((work + 1536), (input + 384), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1539), (input + 387), (9 * sizeof(double)));
    work[1548] = pmDet3by3((work + 1539));
    pmVectorFunction((work + 1549), work, (work + 1548), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1549] = fabs(work[1549]);
    if (work[1549] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W05-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1550), (work + 1539), (work + 1539), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1559), (work + 8), (work + 1550), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1568), (work + 1559), (work + 1559), 9, 1, 9, 1, 1, 1, 3);
    work[1568] = sqrt(work[1568]);
    work[1568] = fabs(work[1568]);
    if (work[1568] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W05-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1539), (work + 1569));
    pmVectorFunction((work + 1578), (input + 396), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1581), (input + 399), (9 * sizeof(double)));
    work[1590] = pmDet3by3((work + 1581));
    pmVectorFunction((work + 1591), work, (work + 1590), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1591] = fabs(work[1591]);
    if (work[1591] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W05-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1592), (work + 1581), (work + 1581), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1601), (work + 8), (work + 1592), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1610), (work + 1601), (work + 1601), 9, 1, 9, 1, 1, 1, 3);
    work[1610] = sqrt(work[1610]);
    work[1610] = fabs(work[1610]);
    if (work[1610] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W05-4: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1581), (work + 1611));
    pmVectorFunction((work + 1620), (input + 371), (work + 1), 0.0, 1.0, 0.0, 1, 1, 1, 0);
    pmVectorFunction((work + 1621), (input + 362), (work + 1), 0.0, 1.0, 0.0, 9, 1, 1, 0);
    memcpy((work + 1630), (work + 1621), (9 * sizeof(double)));
    pmVectorFunction((work + 1639), (input + 292), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1642), (input + 295), (9 * sizeof(double)));
    work[1651] = pmDet3by3((work + 1642));
    pmVectorFunction((work + 1652), work, (work + 1651), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1652] = fabs(work[1652]);
    if (work[1652] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W04-3: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1653), (work + 1642), (work + 1642), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1662), (work + 8), (work + 1653), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1671), (work + 1662), (work + 1662), 9, 1, 9, 1, 1, 1, 3);
    work[1671] = sqrt(work[1671]);
    work[1671] = fabs(work[1671]);
    if (work[1671] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W04-3: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1642), (work + 1672));
    pmVectorFunction((work + 1681), (input + 314), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1684), (input + 317), (9 * sizeof(double)));
    work[1693] = pmDet3by3((work + 1684));
    pmVectorFunction((work + 1694), work, (work + 1693), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1694] = fabs(work[1694]);
    if (work[1694] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W04-3: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1695), (work + 1684), (work + 1684), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1704), (work + 8), (work + 1695), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1713), (work + 1704), (work + 1704), 9, 1, 9, 1, 1, 1, 3);
    work[1713] = sqrt(work[1713]);
    work[1713] = fabs(work[1713]);
    if (work[1713] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W04-3: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1684), (work + 1714));
    pmVectorFunction((work + 1723), (input + 326), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1726), (input + 329), (9 * sizeof(double)));
    work[1735] = pmDet3by3((work + 1726));
    pmVectorFunction((work + 1736), work, (work + 1735), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1736] = fabs(work[1736]);
    if (work[1736] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W04-3: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1737), (work + 1726), (work + 1726), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1746), (work + 8), (work + 1737), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1755), (work + 1746), (work + 1746), 9, 1, 9, 1, 1, 1, 3);
    work[1755] = sqrt(work[1755]);
    work[1755] = fabs(work[1755]);
    if (work[1755] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W04-3: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1726), (work + 1756));
    pmVectorFunction((work + 1765), (input + 338), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1768), (input + 341), (9 * sizeof(double)));
    work[1777] = pmDet3by3((work + 1768));
    pmVectorFunction((work + 1778), work, (work + 1777), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1778] = fabs(work[1778]);
    if (work[1778] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W04-3: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1779), (work + 1768), (work + 1768), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1788), (work + 8), (work + 1779), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1797), (work + 1788), (work + 1788), 9, 1, 9, 1, 1, 1, 3);
    work[1797] = sqrt(work[1797]);
    work[1797] = fabs(work[1797]);
    if (work[1797] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W04-3: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1768), (work + 1798));
    pmVectorFunction((work + 1807), (input + 313), (work + 1), 0.0, 1.0, 0.0, 1, 1, 1, 0);
    pmVectorFunction((work + 1808), (input + 304), (work + 1), 0.0, 1.0, 0.0, 9, 1, 1, 0);
    memcpy((work + 1817), (work + 1808), (9 * sizeof(double)));
    pmVectorFunction((work + 1826), (input + 164), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1829), (input + 167), (9 * sizeof(double)));
    work[1838] = pmDet3by3((work + 1829));
    pmVectorFunction((work + 1839), work, (work + 1838), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1839] = fabs(work[1839]);
    if (work[1839] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W02_1-3: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1840), (work + 1829), (work + 1829), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1849), (work + 8), (work + 1840), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1858), (work + 1849), (work + 1849), 9, 1, 9, 1, 1, 1, 3);
    work[1858] = sqrt(work[1858]);
    work[1858] = fabs(work[1858]);
    if (work[1858] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W02_1-3: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1829), (work + 1859));
    pmVectorFunction((work + 1868), (input + 186), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1871), (input + 189), (9 * sizeof(double)));
    work[1880] = pmDet3by3((work + 1871));
    pmVectorFunction((work + 1881), work, (work + 1880), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1881] = fabs(work[1881]);
    if (work[1881] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W02_1-3: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1882), (work + 1871), (work + 1871), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1891), (work + 8), (work + 1882), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1900), (work + 1891), (work + 1891), 9, 1, 9, 1, 1, 1, 3);
    work[1900] = sqrt(work[1900]);
    work[1900] = fabs(work[1900]);
    if (work[1900] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W02_1-3: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1871), (work + 1901));
    pmVectorFunction((work + 1910), (input + 198), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1913), (input + 201), (9 * sizeof(double)));
    work[1922] = pmDet3by3((work + 1913));
    pmVectorFunction((work + 1923), work, (work + 1922), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1923] = fabs(work[1923]);
    if (work[1923] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W02_1-3: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1924), (work + 1913), (work + 1913), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1933), (work + 8), (work + 1924), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1942), (work + 1933), (work + 1933), 9, 1, 9, 1, 1, 1, 3);
    work[1942] = sqrt(work[1942]);
    work[1942] = fabs(work[1942]);
    if (work[1942] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W02_1-3: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1913), (work + 1943));
    pmVectorFunction((work + 1952), (input + 210), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 1955), (input + 213), (9 * sizeof(double)));
    work[1964] = pmDet3by3((work + 1955));
    pmVectorFunction((work + 1965), work, (work + 1964), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[1965] = fabs(work[1965]);
    if (work[1965] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W02_1-3: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 1966), (work + 1955), (work + 1955), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 1975), (work + 8), (work + 1966), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 1984), (work + 1975), (work + 1975), 9, 1, 9, 1, 1, 1, 3);
    work[1984] = sqrt(work[1984]);
    work[1984] = fabs(work[1984]);
    if (work[1984] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W02_1-3: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 1955), (work + 1985));
    pmVectorFunction((work + 1994), (input + 185), (work + 1), 0.0, 1.0, 0.0, 1, 1, 1, 0);
    pmVectorFunction((work + 1995), (input + 176), (work + 1), 0.0, 1.0, 0.0, 9, 1, 1, 0);
    memcpy((work + 2004), (work + 1995), (9 * sizeof(double)));
    pmVectorFunction((work + 2013), (input + 106), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 2016), (input + 109), (9 * sizeof(double)));
    work[2025] = pmDet3by3((work + 2016));
    pmVectorFunction((work + 2026), work, (work + 2025), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[2026] = fabs(work[2026]);
    if (work[2026] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W01_2-2: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 2027), (work + 2016), (work + 2016), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 2036), (work + 8), (work + 2027), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 2045), (work + 2036), (work + 2036), 9, 1, 9, 1, 1, 1, 3);
    work[2045] = sqrt(work[2045]);
    work[2045] = fabs(work[2045]);
    if (work[2045] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W01_2-2: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 2016), (work + 2046));
    pmVectorFunction((work + 2055), (input + 128), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 2058), (input + 131), (9 * sizeof(double)));
    work[2067] = pmDet3by3((work + 2058));
    pmVectorFunction((work + 2068), work, (work + 2067), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[2068] = fabs(work[2068]);
    if (work[2068] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W01_2-2: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 2069), (work + 2058), (work + 2058), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 2078), (work + 8), (work + 2069), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 2087), (work + 2078), (work + 2078), 9, 1, 9, 1, 1, 1, 3);
    work[2087] = sqrt(work[2087]);
    work[2087] = fabs(work[2087]);
    if (work[2087] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W01_2-2: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 2058), (work + 2088));
    pmVectorFunction((work + 2097), (input + 140), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 2100), (input + 143), (9 * sizeof(double)));
    work[2109] = pmDet3by3((work + 2100));
    pmVectorFunction((work + 2110), work, (work + 2109), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[2110] = fabs(work[2110]);
    if (work[2110] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W01_2-2: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 2111), (work + 2100), (work + 2100), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 2120), (work + 8), (work + 2111), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 2129), (work + 2120), (work + 2120), 9, 1, 9, 1, 1, 1, 3);
    work[2129] = sqrt(work[2129]);
    work[2129] = fabs(work[2129]);
    if (work[2129] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W01_2-2: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 2100), (work + 2130));
    pmVectorFunction((work + 2139), (input + 152), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 2142), (input + 155), (9 * sizeof(double)));
    work[2151] = pmDet3by3((work + 2142));
    pmVectorFunction((work + 2152), work, (work + 2151), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[2152] = fabs(work[2152]);
    if (work[2152] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W01_2-2: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 2153), (work + 2142), (work + 2142), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 2162), (work + 8), (work + 2153), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 2171), (work + 2162), (work + 2162), 9, 1, 9, 1, 1, 1, 3);
    work[2171] = sqrt(work[2171]);
    work[2171] = fabs(work[2171]);
    if (work[2171] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W01_2-2: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 2142), (work + 2172));
    pmVectorFunction((work + 2181), (input + 127), (work + 1), 0.0, 1.0, 0.0, 1, 1, 1, 0);
    pmVectorFunction((work + 2182), (input + 118), (work + 1), 0.0, 1.0, 0.0, 9, 1, 1, 0);
    memcpy((work + 2191), (work + 2182), (9 * sizeof(double)));
    pmVectorFunction((work + 2200), (input + 48), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 2203), (input + 51), (9 * sizeof(double)));
    work[2212] = pmDet3by3((work + 2203));
    pmVectorFunction((work + 2213), work, (work + 2212), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[2213] = fabs(work[2213]);
    if (work[2213] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/RootPart: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 2214), (work + 2203), (work + 2203), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 2223), (work + 8), (work + 2214), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 2232), (work + 2223), (work + 2223), 9, 1, 9, 1, 1, 1, 3);
    work[2232] = sqrt(work[2232]);
    work[2232] = fabs(work[2232]);
    if (work[2232] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/RootPart: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 2203), (work + 2233));
    pmVectorFunction((work + 2242), (input + 70), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 2245), (input + 73), (9 * sizeof(double)));
    work[2254] = pmDet3by3((work + 2245));
    pmVectorFunction((work + 2255), work, (work + 2254), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[2255] = fabs(work[2255]);
    if (work[2255] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/RootPart: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 2256), (work + 2245), (work + 2245), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 2265), (work + 8), (work + 2256), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 2274), (work + 2265), (work + 2265), 9, 1, 9, 1, 1, 1, 3);
    work[2274] = sqrt(work[2274]);
    work[2274] = fabs(work[2274]);
    if (work[2274] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/RootPart: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 2245), (work + 2275));
    pmVectorFunction((work + 2284), (input + 82), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 2287), (input + 85), (9 * sizeof(double)));
    work[2296] = pmDet3by3((work + 2287));
    pmVectorFunction((work + 2297), work, (work + 2296), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[2297] = fabs(work[2297]);
    if (work[2297] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/RootPart: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 2298), (work + 2287), (work + 2287), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 2307), (work + 8), (work + 2298), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 2316), (work + 2307), (work + 2307), 9, 1, 9, 1, 1, 1, 3);
    work[2316] = sqrt(work[2316]);
    work[2316] = fabs(work[2316]);
    if (work[2316] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/RootPart: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 2287), (work + 2317));
    pmVectorFunction((work + 2326), (input + 94), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 2329), (input + 97), (9 * sizeof(double)));
    work[2338] = pmDet3by3((work + 2329));
    pmVectorFunction((work + 2339), work, (work + 2338), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[2339] = fabs(work[2339]);
    if (work[2339] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/RootPart: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 2340), (work + 2329), (work + 2329), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 2349), (work + 8), (work + 2340), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 2358), (work + 2349), (work + 2349), 9, 1, 9, 1, 1, 1, 3);
    work[2358] = sqrt(work[2358]);
    work[2358] = fabs(work[2358]);
    if (work[2358] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/RootPart: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 2329), (work + 2359));
    pmVectorFunction((work + 2368), (input + 69), (work + 1), 0.0, 1.0, 0.0, 1, 1, 1, 0);
    pmVectorFunction((work + 2369), (input + 60), (work + 1), 0.0, 1.0, 0.0, 9, 1, 1, 0);
    memcpy((work + 2378), (work + 2369), (9 * sizeof(double)));
    pmVectorFunction((work + 2387), (input + 222), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 2390), (input + 225), (9 * sizeof(double)));
    work[2399] = pmDet3by3((work + 2390));
    pmVectorFunction((work + 2400), work, (work + 2399), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[2400] = fabs(work[2400]);
    if (work[2400] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W03_1-1: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 2401), (work + 2390), (work + 2390), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 2410), (work + 8), (work + 2401), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 2419), (work + 2410), (work + 2410), 9, 1, 9, 1, 1, 1, 3);
    work[2419] = sqrt(work[2419]);
    work[2419] = fabs(work[2419]);
    if (work[2419] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W03_1-1: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 2390), (work + 2420));
    pmVectorFunction((work + 2429), (input + 244), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 2432), (input + 247), (9 * sizeof(double)));
    work[2441] = pmDet3by3((work + 2432));
    pmVectorFunction((work + 2442), work, (work + 2441), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[2442] = fabs(work[2442]);
    if (work[2442] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W03_1-1: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 2443), (work + 2432), (work + 2432), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 2452), (work + 8), (work + 2443), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 2461), (work + 2452), (work + 2452), 9, 1, 9, 1, 1, 1, 3);
    work[2461] = sqrt(work[2461]);
    work[2461] = fabs(work[2461]);
    if (work[2461] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W03_1-1: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 2432), (work + 2462));
    pmVectorFunction((work + 2471), (input + 256), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 2474), (input + 259), (9 * sizeof(double)));
    work[2483] = pmDet3by3((work + 2474));
    pmVectorFunction((work + 2484), work, (work + 2483), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[2484] = fabs(work[2484]);
    if (work[2484] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W03_1-1: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 2485), (work + 2474), (work + 2474), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 2494), (work + 8), (work + 2485), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 2503), (work + 2494), (work + 2494), 9, 1, 9, 1, 1, 1, 3);
    work[2503] = sqrt(work[2503]);
    work[2503] = fabs(work[2503]);
    if (work[2503] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W03_1-1: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 2474), (work + 2504));
    pmVectorFunction((work + 2513), (input + 268), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 2516), (input + 271), (9 * sizeof(double)));
    work[2525] = pmDet3by3((work + 2516));
    pmVectorFunction((work + 2526), work, (work + 2525), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[2526] = fabs(work[2526]);
    if (work[2526] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W03_1-1: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 2527), (work + 2516), (work + 2516), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 2536), (work + 8), (work + 2527), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 2545), (work + 2536), (work + 2536), 9, 1, 9, 1, 1, 1, 3);
    work[2545] = sqrt(work[2545]);
    work[2545] = fabs(work[2545]);
    if (work[2545] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W03_1-1: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 2516), (work + 2546));
    pmVectorFunction((work + 2555), (input + 280), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 2558), (input + 283), (9 * sizeof(double)));
    work[2567] = pmDet3by3((work + 2558));
    pmVectorFunction((work + 2568), work, (work + 2567), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[2568] = fabs(work[2568]);
    if (work[2568] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W03_1-1: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 2569), (work + 2558), (work + 2558), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 2578), (work + 8), (work + 2569), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 2587), (work + 2578), (work + 2578), 9, 1, 9, 1, 1, 1, 3);
    work[2587] = sqrt(work[2587]);
    work[2587] = fabs(work[2587]);
    if (work[2587] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/W03_1-1: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 2558), (work + 2588));
    pmVectorFunction((work + 2597), (input + 243), (work + 1), 0.0, 1.0, 0.0, 1, 1, 1, 0);
    pmVectorFunction((work + 2598), (input + 234), (work + 1), 0.0, 1.0, 0.0, 9, 1, 1, 0);
    memcpy((work + 2607), (work + 2598), (9 * sizeof(double)));
    pmVectorFunction((work + 2616), (input + 859), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 2619), (input + 862), (9 * sizeof(double)));
    work[2628] = pmDet3by3((work + 2619));
    pmVectorFunction((work + 2629), work, (work + 2628), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[2629] = fabs(work[2629]);
    if (work[2629] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/board-1: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 2630), (work + 2619), (work + 2619), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 2639), (work + 8), (work + 2630), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 2648), (work + 2639), (work + 2639), 9, 1, 9, 1, 1, 1, 3);
    work[2648] = sqrt(work[2648]);
    work[2648] = fabs(work[2648]);
    if (work[2648] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/board-1: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 2619), (work + 2649));
    pmVectorFunction((work + 2658), (input + 881), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 2661), (input + 884), (9 * sizeof(double)));
    work[2670] = pmDet3by3((work + 2661));
    pmVectorFunction((work + 2671), work, (work + 2670), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[2671] = fabs(work[2671]);
    if (work[2671] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/board-1: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 2672), (work + 2661), (work + 2661), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 2681), (work + 8), (work + 2672), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 2690), (work + 2681), (work + 2681), 9, 1, 9, 1, 1, 1, 3);
    work[2690] = sqrt(work[2690]);
    work[2690] = fabs(work[2690]);
    if (work[2690] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/board-1: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 2661), (work + 2691));
    pmVectorFunction((work + 2700), (input + 893), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    memcpy((work + 2703), (input + 896), (9 * sizeof(double)));
    work[2712] = pmDet3by3((work + 2703));
    pmVectorFunction((work + 2713), work, (work + 2712), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[2713] = fabs(work[2713]);
    if (work[2713] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/board-1: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmMult((work + 2714), (work + 2703), (work + 2703), 3, 3, 3, 3, 1, 1, 3);
    pmVectorFunction((work + 2723), (work + 8), (work + 2714), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmMult((work + 2732), (work + 2723), (work + 2723), 9, 1, 9, 1, 1, 1, 3);
    work[2732] = sqrt(work[2732]);
    work[2732] = fabs(work[2732]);
    if (work[2732] >= 0.05000000000000000300)
    {
        strncpy(msg, "MICROBOT_1/board-1: The orientation matrix is not orthonormal, i.e., R'*R = I, det(R) = 1, are not satisfied. Please replace with a valid rotation matrix or use another representation.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmConvertToRotationMatrix(13, (work + 2703), (work + 2733));
    pmVectorFunction((work + 2742), (input + 880), (work + 1), 0.0, 1.0, 0.0, 1, 1, 1, 0);
    pmVectorFunction((work + 2743), (input + 871), (work + 1), 0.0, 1.0, 0.0, 9, 1, 1, 0);
    memcpy((work + 2752), (work + 2743), (9 * sizeof(double)));
    pmMult((work + 2764), (input + 30), (input + 30), 3, 1, 3, 1, 1, 1, 3);
    work[2764] = sqrt(work[2764]);
    if (work[2764] == 0.0)
    {
        strncpy(msg, "MICROBOT_1/Revolute5: Joint primitive R1 has an invalid axis.  Axis must evaluate to a 1-by-3 matrix.  Check and reconfigure primitive axis vector.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    work[2764] = (1.0 / work[2764]);
    pmVectorFunction((work + 2761), (input + 30), (work + 2764), 1.0, 0.0, 0.0, 3, 1, 1, 0);
    pmMult((work + 2768), (input + 6), (input + 6), 3, 1, 3, 1, 1, 1, 3);
    work[2768] = sqrt(work[2768]);
    if (work[2768] == 0.0)
    {
        strncpy(msg, "MICROBOT_1/Cylindrical1: Joint primitive P1 has an invalid axis.  Axis must evaluate to a 1-by-3 matrix.  Check and reconfigure primitive axis vector.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    work[2768] = (1.0 / work[2768]);
    pmVectorFunction((work + 2765), (input + 6), (work + 2768), 1.0, 0.0, 0.0, 3, 1, 1, 0);
    pmMult((work + 2772), (input + 9), (input + 9), 3, 1, 3, 1, 1, 1, 3);
    work[2772] = sqrt(work[2772]);
    if (work[2772] == 0.0)
    {
        strncpy(msg, "MICROBOT_1/Cylindrical1: Joint primitive R1 has an invalid axis.  Axis must evaluate to a 1-by-3 matrix.  Check and reconfigure primitive axis vector.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    work[2772] = (1.0 / work[2772]);
    pmVectorFunction((work + 2769), (input + 9), (work + 2772), 1.0, 0.0, 0.0, 3, 1, 1, 0);
    pmMult((work + 2776), (input + 18), (input + 18), 3, 1, 3, 1, 1, 1, 3);
    work[2776] = sqrt(work[2776]);
    if (work[2776] == 0.0)
    {
        strncpy(msg, "MICROBOT_1/Revolute10: Joint primitive R1 has an invalid axis.  Axis must evaluate to a 1-by-3 matrix.  Check and reconfigure primitive axis vector.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    work[2776] = (1.0 / work[2776]);
    pmVectorFunction((work + 2773), (input + 18), (work + 2776), 1.0, 0.0, 0.0, 3, 1, 1, 0);
    pmMult((work + 2780), (input + 33), (input + 33), 3, 1, 3, 1, 1, 1, 3);
    work[2780] = sqrt(work[2780]);
    if (work[2780] == 0.0)
    {
        strncpy(msg, "MICROBOT_1/Revolute6: Joint primitive R1 has an invalid axis.  Axis must evaluate to a 1-by-3 matrix.  Check and reconfigure primitive axis vector.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    work[2780] = (1.0 / work[2780]);
    pmVectorFunction((work + 2777), (input + 33), (work + 2780), 1.0, 0.0, 0.0, 3, 1, 1, 0);
    pmMult((work + 2784), (input + 21), (input + 21), 3, 1, 3, 1, 1, 1, 3);
    work[2784] = sqrt(work[2784]);
    if (work[2784] == 0.0)
    {
        strncpy(msg, "MICROBOT_1/Revolute2: Joint primitive R1 has an invalid axis.  Axis must evaluate to a 1-by-3 matrix.  Check and reconfigure primitive axis vector.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    work[2784] = (1.0 / work[2784]);
    pmVectorFunction((work + 2781), (input + 21), (work + 2784), 1.0, 0.0, 0.0, 3, 1, 1, 0);
    pmMult((work + 2788), input, input, 3, 1, 3, 1, 1, 1, 3);
    work[2788] = sqrt(work[2788]);
    if (work[2788] == 0.0)
    {
        strncpy(msg, "MICROBOT_1/Cylindrical: Joint primitive P1 has an invalid axis.  Axis must evaluate to a 1-by-3 matrix.  Check and reconfigure primitive axis vector.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    work[2788] = (1.0 / work[2788]);
    pmVectorFunction((work + 2785), input, (work + 2788), 1.0, 0.0, 0.0, 3, 1, 1, 0);
    pmMult((work + 2792), (input + 3), (input + 3), 3, 1, 3, 1, 1, 1, 3);
    work[2792] = sqrt(work[2792]);
    if (work[2792] == 0.0)
    {
        strncpy(msg, "MICROBOT_1/Cylindrical: Joint primitive R1 has an invalid axis.  Axis must evaluate to a 1-by-3 matrix.  Check and reconfigure primitive axis vector.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    work[2792] = (1.0 / work[2792]);
    pmVectorFunction((work + 2789), (input + 3), (work + 2792), 1.0, 0.0, 0.0, 3, 1, 1, 0);
    pmMult((work + 2796), (input + 42), (input + 42), 3, 1, 3, 1, 1, 1, 3);
    work[2796] = sqrt(work[2796]);
    if (work[2796] == 0.0)
    {
        strncpy(msg, "MICROBOT_1/Revolute9: Joint primitive R1 has an invalid axis.  Axis must evaluate to a 1-by-3 matrix.  Check and reconfigure primitive axis vector.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    work[2796] = (1.0 / work[2796]);
    pmVectorFunction((work + 2793), (input + 42), (work + 2796), 1.0, 0.0, 0.0, 3, 1, 1, 0);
    pmMult((work + 2800), (input + 36), (input + 36), 3, 1, 3, 1, 1, 1, 3);
    work[2800] = sqrt(work[2800]);
    if (work[2800] == 0.0)
    {
        strncpy(msg, "MICROBOT_1/Revolute7: Joint primitive R1 has an invalid axis.  Axis must evaluate to a 1-by-3 matrix.  Check and reconfigure primitive axis vector.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    work[2800] = (1.0 / work[2800]);
    pmVectorFunction((work + 2797), (input + 36), (work + 2800), 1.0, 0.0, 0.0, 3, 1, 1, 0);
    pmMult((work + 2804), (input + 15), (input + 15), 3, 1, 3, 1, 1, 1, 3);
    work[2804] = sqrt(work[2804]);
    if (work[2804] == 0.0)
    {
        strncpy(msg, "MICROBOT_1/Revolute1: Joint primitive R1 has an invalid axis.  Axis must evaluate to a 1-by-3 matrix.  Check and reconfigure primitive axis vector.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    work[2804] = (1.0 / work[2804]);
    pmVectorFunction((work + 2801), (input + 15), (work + 2804), 1.0, 0.0, 0.0, 3, 1, 1, 0);
    pmMult((work + 2808), (input + 12), (input + 12), 3, 1, 3, 1, 1, 1, 3);
    work[2808] = sqrt(work[2808]);
    if (work[2808] == 0.0)
    {
        strncpy(msg, "MICROBOT_1/Revolute: Joint primitive R1 has an invalid axis.  Axis must evaluate to a 1-by-3 matrix.  Check and reconfigure primitive axis vector.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    work[2808] = (1.0 / work[2808]);
    pmVectorFunction((work + 2805), (input + 12), (work + 2808), 1.0, 0.0, 0.0, 3, 1, 1, 0);
    pmMult((work + 2812), (input + 24), (input + 24), 3, 1, 3, 1, 1, 1, 3);
    work[2812] = sqrt(work[2812]);
    if (work[2812] == 0.0)
    {
        strncpy(msg, "MICROBOT_1/Revolute3: Joint primitive R1 has an invalid axis.  Axis must evaluate to a 1-by-3 matrix.  Check and reconfigure primitive axis vector.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    work[2812] = (1.0 / work[2812]);
    pmVectorFunction((work + 2809), (input + 24), (work + 2812), 1.0, 0.0, 0.0, 3, 1, 1, 0);
    pmMult((work + 2816), (input + 39), (input + 39), 3, 1, 3, 1, 1, 1, 3);
    work[2816] = sqrt(work[2816]);
    if (work[2816] == 0.0)
    {
        strncpy(msg, "MICROBOT_1/Revolute8: Joint primitive R1 has an invalid axis.  Axis must evaluate to a 1-by-3 matrix.  Check and reconfigure primitive axis vector.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    work[2816] = (1.0 / work[2816]);
    pmVectorFunction((work + 2813), (input + 39), (work + 2816), 1.0, 0.0, 0.0, 3, 1, 1, 0);
    pmMult((work + 2820), (input + 27), (input + 27), 3, 1, 3, 1, 1, 1, 3);
    work[2820] = sqrt(work[2820]);
    if (work[2820] == 0.0)
    {
        strncpy(msg, "MICROBOT_1/Revolute4: Joint primitive R1 has an invalid axis.  Axis must evaluate to a 1-by-3 matrix.  Check and reconfigure primitive axis vector.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    work[2820] = (1.0 / work[2820]);
    pmVectorFunction((work + 2817), (input + 27), (work + 2820), 1.0, 0.0, 0.0, 3, 1, 1, 0);
    pmVectorFunction((work + 2824), (input + 45), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    pmVectorFunction((work + 2827), (work + 2821), (work + 1), 0.0, 0.01745329251994329500, 0.0, 3, 1, 1, 0);
    pmConvertToRotationMatrix(1, (work + 2827), (work + 2830));
    pmVectorFunction((work + 2855), (work + 2849), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    pmVectorFunction((work + 2858), (work + 2852), (work + 1), 0.0, 0.01745329251994329500, 0.0, 3, 1, 1, 0);
    pmConvertToRotationMatrix(1, (work + 2858), (work + 2861));
    pmVectorFunction((work + 2870), (input + 45), (work + 1), 0.0, 1.0, 0.0, 3, 1, 1, 0);
    pmVectorFunction((work + 2873), (work + 2821), (work + 1), 0.0, 0.01745329251994329500, 0.0, 3, 1, 1, 0);
    pmConvertToRotationMatrix(0, (work + 2873), (work + 2876));
    pmVectorFunction((work + 2885), (work + 2839), (work + 1), 0.0, 1.0, 0.0, 1, 1, 1, 0);
    pmVectorFunction((work + 2886), (work + 2840), (work + 1), 0.0, 1.0, 0.0, 9, 1, 1, 0);
    memcpy((work + 2895), (work + 2886), (9 * sizeof(double)));
    pmVectorFunction((work + 2904), (work + 2855), (work + 1), 0.0, -1.0, 0.0, 3, 1, 1, 0);
    pmVectorFunction((work + 2907), (work + 17), (work + 101), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    pmMult((work + 2910), (work + 186), (work + 50), 3, 3, 3, 3, 1, 1, 2);
    pmMult((work + 186), (work + 50), (work + 2910), 3, 3, 3, 3, 1, 1, 1);
    pmMult((work + 2928), (work + 2907), (work + 2907), 3, 1, 3, 1, 1, 1, 3);
    pmVectorFunction((work + 2910), (work + 8), (work + 2928), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmMult((work + 2919), (work + 2907), (work + 2907), 3, 1, 3, 1, 1, 1, 2);
    pmVectorFunction((work + 2910), (work + 2910), (work + 2919), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 2910), (work + 2910), (work + 185), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmVectorFunction((work + 186), (work + 186), (work + 2910), 0.0, 1.0, 1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 2938), (work + 204), (work + 330), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    pmMult((work + 2941), (work + 373), (work + 237), 3, 3, 3, 3, 1, 1, 2);
    pmMult((work + 373), (work + 237), (work + 2941), 3, 3, 3, 3, 1, 1, 1);
    pmMult((work + 2959), (work + 2938), (work + 2938), 3, 1, 3, 1, 1, 1, 3);
    pmVectorFunction((work + 2941), (work + 8), (work + 2959), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmMult((work + 2950), (work + 2938), (work + 2938), 3, 1, 3, 1, 1, 1, 2);
    pmVectorFunction((work + 2941), (work + 2941), (work + 2950), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 2941), (work + 2941), (work + 372), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmVectorFunction((work + 373), (work + 373), (work + 2941), 0.0, 1.0, 1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 2969), (work + 391), (work + 475), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    pmMult((work + 2972), (work + 560), (work + 424), 3, 3, 3, 3, 1, 1, 2);
    pmMult((work + 560), (work + 424), (work + 2972), 3, 3, 3, 3, 1, 1, 1);
    pmMult((work + 2990), (work + 2969), (work + 2969), 3, 1, 3, 1, 1, 1, 3);
    pmVectorFunction((work + 2972), (work + 8), (work + 2990), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmMult((work + 2981), (work + 2969), (work + 2969), 3, 1, 3, 1, 1, 1, 2);
    pmVectorFunction((work + 2972), (work + 2972), (work + 2981), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 2972), (work + 2972), (work + 559), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmVectorFunction((work + 560), (work + 560), (work + 2972), 0.0, 1.0, 1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3000), (work + 578), (work + 662), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    pmMult((work + 3003), (work + 747), (work + 611), 3, 3, 3, 3, 1, 1, 2);
    pmMult((work + 747), (work + 611), (work + 3003), 3, 3, 3, 3, 1, 1, 1);
    pmMult((work + 3021), (work + 3000), (work + 3000), 3, 1, 3, 1, 1, 1, 3);
    pmVectorFunction((work + 3003), (work + 8), (work + 3021), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmMult((work + 3012), (work + 3000), (work + 3000), 3, 1, 3, 1, 1, 1, 2);
    pmVectorFunction((work + 3003), (work + 3003), (work + 3012), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3003), (work + 3003), (work + 746), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmVectorFunction((work + 747), (work + 747), (work + 3003), 0.0, 1.0, 1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3031), (work + 765), (work + 891), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    pmMult((work + 3034), (work + 934), (work + 798), 3, 3, 3, 3, 1, 1, 2);
    pmMult((work + 934), (work + 798), (work + 3034), 3, 3, 3, 3, 1, 1, 1);
    pmMult((work + 3052), (work + 3031), (work + 3031), 3, 1, 3, 1, 1, 1, 3);
    pmVectorFunction((work + 3034), (work + 8), (work + 3052), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmMult((work + 3043), (work + 3031), (work + 3031), 3, 1, 3, 1, 1, 1, 2);
    pmVectorFunction((work + 3034), (work + 3034), (work + 3043), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3034), (work + 3034), (work + 933), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmVectorFunction((work + 934), (work + 934), (work + 3034), 0.0, 1.0, 1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3062), (work + 952), (work + 1036), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    pmMult((work + 3065), (work + 1121), (work + 985), 3, 3, 3, 3, 1, 1, 2);
    pmMult((work + 1121), (work + 985), (work + 3065), 3, 3, 3, 3, 1, 1, 1);
    pmMult((work + 3083), (work + 3062), (work + 3062), 3, 1, 3, 1, 1, 1, 3);
    pmVectorFunction((work + 3065), (work + 8), (work + 3083), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmMult((work + 3074), (work + 3062), (work + 3062), 3, 1, 3, 1, 1, 1, 2);
    pmVectorFunction((work + 3065), (work + 3065), (work + 3074), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3065), (work + 3065), (work + 1120), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmVectorFunction((work + 1121), (work + 1121), (work + 3065), 0.0, 1.0, 1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3093), (work + 1139), (work + 1223), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    pmMult((work + 3096), (work + 1434), (work + 1172), 3, 3, 3, 3, 1, 1, 2);
    pmMult((work + 1434), (work + 1172), (work + 3096), 3, 3, 3, 3, 1, 1, 1);
    pmMult((work + 3114), (work + 3093), (work + 3093), 3, 1, 3, 1, 1, 1, 3);
    pmVectorFunction((work + 3096), (work + 8), (work + 3114), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmMult((work + 3105), (work + 3093), (work + 3093), 3, 1, 3, 1, 1, 1, 2);
    pmVectorFunction((work + 3096), (work + 3096), (work + 3105), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3096), (work + 3096), (work + 1433), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmVectorFunction((work + 1434), (work + 1434), (work + 3096), 0.0, 1.0, 1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3124), (work + 1452), (work + 1536), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    pmMult((work + 3127), (work + 1621), (work + 1485), 3, 3, 3, 3, 1, 1, 2);
    pmMult((work + 1621), (work + 1485), (work + 3127), 3, 3, 3, 3, 1, 1, 1);
    pmMult((work + 3145), (work + 3124), (work + 3124), 3, 1, 3, 1, 1, 1, 3);
    pmVectorFunction((work + 3127), (work + 8), (work + 3145), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmMult((work + 3136), (work + 3124), (work + 3124), 3, 1, 3, 1, 1, 1, 2);
    pmVectorFunction((work + 3127), (work + 3127), (work + 3136), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3127), (work + 3127), (work + 1620), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmVectorFunction((work + 1621), (work + 1621), (work + 3127), 0.0, 1.0, 1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3155), (work + 1639), (work + 1765), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    pmMult((work + 3158), (work + 1808), (work + 1672), 3, 3, 3, 3, 1, 1, 2);
    pmMult((work + 1808), (work + 1672), (work + 3158), 3, 3, 3, 3, 1, 1, 1);
    pmMult((work + 3176), (work + 3155), (work + 3155), 3, 1, 3, 1, 1, 1, 3);
    pmVectorFunction((work + 3158), (work + 8), (work + 3176), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmMult((work + 3167), (work + 3155), (work + 3155), 3, 1, 3, 1, 1, 1, 2);
    pmVectorFunction((work + 3158), (work + 3158), (work + 3167), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3158), (work + 3158), (work + 1807), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmVectorFunction((work + 1808), (work + 1808), (work + 3158), 0.0, 1.0, 1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3186), (work + 1826), (work + 1952), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    pmMult((work + 3189), (work + 1995), (work + 1859), 3, 3, 3, 3, 1, 1, 2);
    pmMult((work + 1995), (work + 1859), (work + 3189), 3, 3, 3, 3, 1, 1, 1);
    pmMult((work + 3207), (work + 3186), (work + 3186), 3, 1, 3, 1, 1, 1, 3);
    pmVectorFunction((work + 3189), (work + 8), (work + 3207), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmMult((work + 3198), (work + 3186), (work + 3186), 3, 1, 3, 1, 1, 1, 2);
    pmVectorFunction((work + 3189), (work + 3189), (work + 3198), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3189), (work + 3189), (work + 1994), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmVectorFunction((work + 1995), (work + 1995), (work + 3189), 0.0, 1.0, 1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3217), (work + 2013), (work + 2097), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    pmMult((work + 3220), (work + 2182), (work + 2046), 3, 3, 3, 3, 1, 1, 2);
    pmMult((work + 2182), (work + 2046), (work + 3220), 3, 3, 3, 3, 1, 1, 1);
    pmMult((work + 3238), (work + 3217), (work + 3217), 3, 1, 3, 1, 1, 1, 3);
    pmVectorFunction((work + 3220), (work + 8), (work + 3238), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmMult((work + 3229), (work + 3217), (work + 3217), 3, 1, 3, 1, 1, 1, 2);
    pmVectorFunction((work + 3220), (work + 3220), (work + 3229), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3220), (work + 3220), (work + 2181), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmVectorFunction((work + 2182), (work + 2182), (work + 3220), 0.0, 1.0, 1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3248), (work + 2200), (work + 2326), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    pmMult((work + 3251), (work + 2369), (work + 2233), 3, 3, 3, 3, 1, 1, 2);
    pmMult((work + 2369), (work + 2233), (work + 3251), 3, 3, 3, 3, 1, 1, 1);
    pmMult((work + 3269), (work + 3248), (work + 3248), 3, 1, 3, 1, 1, 1, 3);
    pmVectorFunction((work + 3251), (work + 8), (work + 3269), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmMult((work + 3260), (work + 3248), (work + 3248), 3, 1, 3, 1, 1, 1, 2);
    pmVectorFunction((work + 3251), (work + 3251), (work + 3260), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3251), (work + 3251), (work + 2368), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmVectorFunction((work + 2369), (work + 2369), (work + 3251), 0.0, 1.0, 1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3279), (work + 2387), (work + 2471), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    pmMult((work + 3282), (work + 2598), (work + 2420), 3, 3, 3, 3, 1, 1, 2);
    pmMult((work + 2598), (work + 2420), (work + 3282), 3, 3, 3, 3, 1, 1, 1);
    pmMult((work + 3300), (work + 3279), (work + 3279), 3, 1, 3, 1, 1, 1, 3);
    pmVectorFunction((work + 3282), (work + 8), (work + 3300), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmMult((work + 3291), (work + 3279), (work + 3279), 3, 1, 3, 1, 1, 1, 2);
    pmVectorFunction((work + 3282), (work + 3282), (work + 3291), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3282), (work + 3282), (work + 2597), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmVectorFunction((work + 2598), (work + 2598), (work + 3282), 0.0, 1.0, 1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3310), (work + 2616), (work + 2700), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    pmMult((work + 3313), (work + 2743), (work + 2649), 3, 3, 3, 3, 1, 1, 2);
    pmMult((work + 2743), (work + 2649), (work + 3313), 3, 3, 3, 3, 1, 1, 1);
    pmMult((work + 3331), (work + 3310), (work + 3310), 3, 1, 3, 1, 1, 1, 3);
    pmVectorFunction((work + 3313), (work + 8), (work + 3331), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmMult((work + 3322), (work + 3310), (work + 3310), 3, 1, 3, 1, 1, 1, 2);
    pmVectorFunction((work + 3313), (work + 3313), (work + 3322), 0.0, 1.0, -1.0, 9, 1, 1, 1);
    pmVectorFunction((work + 3313), (work + 3313), (work + 2742), 1.0, 0.0, 0.0, 9, 1, 1, 0);
    pmVectorFunction((work + 2743), (work + 2743), (work + 3313), 0.0, 1.0, 1.0, 9, 1, 1, 1);
    work[3341] = work[1];
    work[3342] = work[1];
    work[3343] = work[1];
    pmVectorFunction((work + 3344), (work + 101), (work + 1307), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    work[3347] = work[1];
    work[3348] = work[1];
    work[3349] = work[1];
    pmVectorFunction((work + 3350), (work + 330), (work + 517), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    work[3353] = work[1];
    work[3354] = work[1];
    work[3355] = work[1];
    pmVectorFunction((work + 3356), (work + 475), (work + 1349), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    work[3359] = work[1];
    work[3360] = work[1];
    work[3361] = work[1];
    pmVectorFunction((work + 3362), (work + 662), (work + 1265), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    work[3365] = work[1];
    work[3366] = work[1];
    work[3367] = work[1];
    pmVectorFunction((work + 3368), (work + 891), (work + 1078), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    work[3371] = work[1];
    work[3372] = work[1];
    work[3373] = work[1];
    pmVectorFunction((work + 3374), (work + 1036), (work + 1391), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    work[3377] = work[1];
    work[3378] = work[1];
    work[3379] = work[1];
    pmVectorFunction((work + 3380), (work + 1223), (work + 1578), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    work[3383] = work[1];
    work[3384] = work[1];
    work[3385] = work[1];
    pmVectorFunction((work + 3386), (work + 1536), (work + 1723), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    work[3389] = work[1];
    work[3390] = work[1];
    work[3391] = work[1];
    pmVectorFunction((work + 3392), (work + 1765), (work + 1910), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    work[3395] = work[1];
    work[3396] = work[1];
    work[3397] = work[1];
    pmVectorFunction((work + 3398), (work + 1952), (work + 2139), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    work[3401] = work[1];
    work[3402] = work[1];
    work[3403] = work[1];
    pmVectorFunction((work + 3404), (work + 2097), (work + 2513), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    work[3407] = work[1];
    work[3408] = work[1];
    work[3409] = work[1];
    pmVectorFunction((work + 3410), (work + 2326), (work + 2870), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    work[3413] = work[1];
    work[3414] = work[1];
    work[3415] = work[1];
    pmVectorFunction((work + 3416), (work + 2471), (work + 2284), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    work[3419] = work[1];
    work[3420] = work[1];
    work[3421] = work[1];
    pmVectorFunction((work + 3422), (work + 2700), (work + 2555), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    work[3425] = work[1];
    work[3426] = work[1];
    work[3427] = work[1];
    pmVectorFunction((work + 3428), (work + 704), (work + 662), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    pmVectorFunction((work + 3431), (work + 849), (work + 891), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    work[3434] = work[1];
    work[3435] = work[1];
    work[3436] = work[1];
    work[3437] = work[1];
    work[3438] = work[1];
    work[3439] = work[1];
    pmMult((work + 3440), (work + 2789), (work + 2785), 3, 1, 3, 1, 1, 1, 3);
    work[3440] = fabs(work[3440]);
    work[3440] = sqrt(work[3440]);
    pmVectorFunction((work + 3441), work, (work + 3440), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[3441] = fabs(work[3441]);
    if (work[3441] >= 0.00100000000000000000)
    {
        strncpy(msg, "MICROBOT_1/Cylindrical: Prismatic and revolute axes of the Cylindrical Joint are not aligned.  Reconfigure axes to be aligned.  If axes are referenced to base or follower, check Body coordinate systems on adjoining bodies.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    pmVectorFunction((work + 3442), (work + 143), (work + 101), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    pmVectorFunction((work + 3445), (work + 288), (work + 330), 0.0, 1.0, -1.0, 3, 1, 1, 1);
    work[3448] = work[1];
    work[3449] = work[1];
    work[3450] = work[1];
    work[3451] = work[1];
    work[3452] = work[1];
    work[3453] = work[1];
    pmMult((work + 3454), (work + 2769), (work + 2765), 3, 1, 3, 1, 1, 1, 3);
    work[3454] = fabs(work[3454]);
    work[3454] = sqrt(work[3454]);
    pmVectorFunction((work + 3455), work, (work + 3454), 0.0, 1.0, -1.0, 1, 1, 1, 1);
    work[3455] = fabs(work[3455]);
    if (work[3455] >= 0.00100000000000000000)
    {
        strncpy(msg, "MICROBOT_1/Cylindrical1: Prismatic and revolute axes of the Cylindrical Joint are not aligned.  Reconfigure axes to be aligned.  If axes are referenced to base or follower, check Body coordinate systems on adjoining bodies.", msg_size);
        error = 1;
        goto EXIT_POINT;
    }
    output[0] = work[185];
    memcpy((output + 1), (work + 195), (9 * sizeof(double)));
    output[10] = work[372];
    memcpy((output + 11), (work + 382), (9 * sizeof(double)));
    output[20] = work[559];
    memcpy((output + 21), (work + 569), (9 * sizeof(double)));
    output[30] = work[746];
    memcpy((output + 31), (work + 756), (9 * sizeof(double)));
    output[40] = work[933];
    memcpy((output + 41), (work + 943), (9 * sizeof(double)));
    output[50] = work[1120];
    memcpy((output + 51), (work + 1130), (9 * sizeof(double)));
    output[60] = work[1433];
    memcpy((output + 61), (work + 1443), (9 * sizeof(double)));
    output[70] = work[1620];
    memcpy((output + 71), (work + 1630), (9 * sizeof(double)));
    output[80] = work[1807];
    memcpy((output + 81), (work + 1817), (9 * sizeof(double)));
    output[90] = work[1994];
    memcpy((output + 91), (work + 2004), (9 * sizeof(double)));
    output[100] = work[2181];
    memcpy((output + 101), (work + 2191), (9 * sizeof(double)));
    output[110] = work[2368];
    memcpy((output + 111), (work + 2378), (9 * sizeof(double)));
    output[120] = work[2597];
    memcpy((output + 121), (work + 2607), (9 * sizeof(double)));
    output[130] = work[2742];
    memcpy((output + 131), (work + 2752), (9 * sizeof(double)));
    output[140] = work[2885];
    memcpy((output + 141), (work + 2895), (9 * sizeof(double)));
    memcpy((output + 150), (work + 2861), (9 * sizeof(double)));
    memcpy((output + 159), (work + 2876), (9 * sizeof(double)));
    memcpy((output + 168), (work + 50), (9 * sizeof(double)));
    memcpy((output + 177), (work + 92), (9 * sizeof(double)));
    memcpy((output + 186), (work + 134), (9 * sizeof(double)));
    memcpy((output + 195), (work + 176), (9 * sizeof(double)));
    memcpy((output + 204), (work + 237), (9 * sizeof(double)));
    memcpy((output + 213), (work + 279), (9 * sizeof(double)));
    memcpy((output + 222), (work + 321), (9 * sizeof(double)));
    memcpy((output + 231), (work + 363), (9 * sizeof(double)));
    memcpy((output + 240), (work + 424), (9 * sizeof(double)));
    memcpy((output + 249), (work + 466), (9 * sizeof(double)));
    memcpy((output + 258), (work + 508), (9 * sizeof(double)));
    memcpy((output + 267), (work + 550), (9 * sizeof(double)));
    memcpy((output + 276), (work + 611), (9 * sizeof(double)));
    memcpy((output + 285), (work + 653), (9 * sizeof(double)));
    memcpy((output + 294), (work + 695), (9 * sizeof(double)));
    memcpy((output + 303), (work + 737), (9 * sizeof(double)));
    memcpy((output + 312), (work + 798), (9 * sizeof(double)));
    memcpy((output + 321), (work + 840), (9 * sizeof(double)));
    memcpy((output + 330), (work + 882), (9 * sizeof(double)));
    memcpy((output + 339), (work + 924), (9 * sizeof(double)));
    memcpy((output + 348), (work + 985), (9 * sizeof(double)));
    memcpy((output + 357), (work + 1027), (9 * sizeof(double)));
    memcpy((output + 366), (work + 1069), (9 * sizeof(double)));
    memcpy((output + 375), (work + 1111), (9 * sizeof(double)));
    memcpy((output + 384), (work + 1172), (9 * sizeof(double)));
    memcpy((output + 393), (work + 1214), (9 * sizeof(double)));
    memcpy((output + 402), (work + 1256), (9 * sizeof(double)));
    memcpy((output + 411), (work + 1298), (9 * sizeof(double)));
    memcpy((output + 420), (work + 1340), (9 * sizeof(double)));
    memcpy((output + 429), (work + 1382), (9 * sizeof(double)));
    memcpy((output + 438), (work + 1424), (9 * sizeof(double)));
    memcpy((output + 447), (work + 1485), (9 * sizeof(double)));
    memcpy((output + 456), (work + 1527), (9 * sizeof(double)));
    memcpy((output + 465), (work + 1569), (9 * sizeof(double)));
    memcpy((output + 474), (work + 1611), (9 * sizeof(double)));
    memcpy((output + 483), (work + 1672), (9 * sizeof(double)));
    memcpy((output + 492), (work + 1714), (9 * sizeof(double)));
    memcpy((output + 501), (work + 1756), (9 * sizeof(double)));
    memcpy((output + 510), (work + 1798), (9 * sizeof(double)));
    memcpy((output + 519), (work + 1859), (9 * sizeof(double)));
    memcpy((output + 528), (work + 1901), (9 * sizeof(double)));
    memcpy((output + 537), (work + 1943), (9 * sizeof(double)));
    memcpy((output + 546), (work + 1985), (9 * sizeof(double)));
    memcpy((output + 555), (work + 2046), (9 * sizeof(double)));
    memcpy((output + 564), (work + 2088), (9 * sizeof(double)));
    memcpy((output + 573), (work + 2130), (9 * sizeof(double)));
    memcpy((output + 582), (work + 2172), (9 * sizeof(double)));
    memcpy((output + 591), (work + 2233), (9 * sizeof(double)));
    memcpy((output + 600), (work + 2275), (9 * sizeof(double)));
    memcpy((output + 609), (work + 2317), (9 * sizeof(double)));
    memcpy((output + 618), (work + 2359), (9 * sizeof(double)));
    memcpy((output + 627), (work + 2420), (9 * sizeof(double)));
    memcpy((output + 636), (work + 2462), (9 * sizeof(double)));
    memcpy((output + 645), (work + 2504), (9 * sizeof(double)));
    memcpy((output + 654), (work + 2546), (9 * sizeof(double)));
    memcpy((output + 663), (work + 2588), (9 * sizeof(double)));
    memcpy((output + 672), (work + 2649), (9 * sizeof(double)));
    memcpy((output + 681), (work + 2691), (9 * sizeof(double)));
    memcpy((output + 690), (work + 2733), (9 * sizeof(double)));
    memcpy((output + 699), (work + 2830), (9 * sizeof(double)));
    memcpy((output + 708), (work + 2855), (3 * sizeof(double)));
    memcpy((output + 711), (work + 2870), (3 * sizeof(double)));
    memcpy((output + 714), (work + 17), (3 * sizeof(double)));
    memcpy((output + 717), (work + 59), (3 * sizeof(double)));
    memcpy((output + 720), (work + 101), (3 * sizeof(double)));
    memcpy((output + 723), (work + 143), (3 * sizeof(double)));
    memcpy((output + 726), (work + 204), (3 * sizeof(double)));
    memcpy((output + 729), (work + 246), (3 * sizeof(double)));
    memcpy((output + 732), (work + 288), (3 * sizeof(double)));
    memcpy((output + 735), (work + 330), (3 * sizeof(double)));
    memcpy((output + 738), (work + 391), (3 * sizeof(double)));
    memcpy((output + 741), (work + 433), (3 * sizeof(double)));
    memcpy((output + 744), (work + 475), (3 * sizeof(double)));
    memcpy((output + 747), (work + 517), (3 * sizeof(double)));
    memcpy((output + 750), (work + 578), (3 * sizeof(double)));
    memcpy((output + 753), (work + 620), (3 * sizeof(double)));
    memcpy((output + 756), (work + 662), (3 * sizeof(double)));
    memcpy((output + 759), (work + 704), (3 * sizeof(double)));
    memcpy((output + 762), (work + 765), (3 * sizeof(double)));
    memcpy((output + 765), (work + 807), (3 * sizeof(double)));
    memcpy((output + 768), (work + 849), (3 * sizeof(double)));
    memcpy((output + 771), (work + 891), (3 * sizeof(double)));
    memcpy((output + 774), (work + 952), (3 * sizeof(double)));
    memcpy((output + 777), (work + 994), (3 * sizeof(double)));
    memcpy((output + 780), (work + 1036), (3 * sizeof(double)));
    memcpy((output + 783), (work + 1078), (3 * sizeof(double)));
    memcpy((output + 786), (work + 1139), (3 * sizeof(double)));
    memcpy((output + 789), (work + 1181), (3 * sizeof(double)));
    memcpy((output + 792), (work + 1223), (3 * sizeof(double)));
    memcpy((output + 795), (work + 1265), (3 * sizeof(double)));
    memcpy((output + 798), (work + 1307), (3 * sizeof(double)));
    memcpy((output + 801), (work + 1349), (3 * sizeof(double)));
    memcpy((output + 804), (work + 1391), (3 * sizeof(double)));
    memcpy((output + 807), (work + 1452), (3 * sizeof(double)));
    memcpy((output + 810), (work + 1494), (3 * sizeof(double)));
    memcpy((output + 813), (work + 1536), (3 * sizeof(double)));
    memcpy((output + 816), (work + 1578), (3 * sizeof(double)));
    memcpy((output + 819), (work + 1639), (3 * sizeof(double)));
    memcpy((output + 822), (work + 1681), (3 * sizeof(double)));
    memcpy((output + 825), (work + 1723), (3 * sizeof(double)));
    memcpy((output + 828), (work + 1765), (3 * sizeof(double)));
    memcpy((output + 831), (work + 1826), (3 * sizeof(double)));
    memcpy((output + 834), (work + 1868), (3 * sizeof(double)));
    memcpy((output + 837), (work + 1910), (3 * sizeof(double)));
    memcpy((output + 840), (work + 1952), (3 * sizeof(double)));
    memcpy((output + 843), (work + 2013), (3 * sizeof(double)));
    memcpy((output + 846), (work + 2055), (3 * sizeof(double)));
    memcpy((output + 849), (work + 2097), (3 * sizeof(double)));
    memcpy((output + 852), (work + 2139), (3 * sizeof(double)));
    memcpy((output + 855), (work + 2200), (3 * sizeof(double)));
    memcpy((output + 858), (work + 2242), (3 * sizeof(double)));
    memcpy((output + 861), (work + 2284), (3 * sizeof(double)));
    memcpy((output + 864), (work + 2326), (3 * sizeof(double)));
    memcpy((output + 867), (work + 2387), (3 * sizeof(double)));
    memcpy((output + 870), (work + 2429), (3 * sizeof(double)));
    memcpy((output + 873), (work + 2471), (3 * sizeof(double)));
    memcpy((output + 876), (work + 2513), (3 * sizeof(double)));
    memcpy((output + 879), (work + 2555), (3 * sizeof(double)));
    memcpy((output + 882), (work + 2616), (3 * sizeof(double)));
    memcpy((output + 885), (work + 2658), (3 * sizeof(double)));
    memcpy((output + 888), (work + 2700), (3 * sizeof(double)));
    memcpy((output + 891), (work + 2824), (3 * sizeof(double)));
    memcpy((output + 894), (work + 2904), (3 * sizeof(double)));
    output[897] = work[1];
    memcpy((output + 898), (work + 8), (9 * sizeof(double)));
    output[907] = work[185];
    memcpy((output + 908), (work + 186), (9 * sizeof(double)));
    memcpy((output + 917), (work + 2907), (3 * sizeof(double)));
    memcpy((output + 920), (work + 2929), (9 * sizeof(double)));
    output[929] = work[372];
    memcpy((output + 930), (work + 373), (9 * sizeof(double)));
    memcpy((output + 939), (work + 2938), (3 * sizeof(double)));
    memcpy((output + 942), (work + 2960), (9 * sizeof(double)));
    output[951] = work[559];
    memcpy((output + 952), (work + 560), (9 * sizeof(double)));
    memcpy((output + 961), (work + 2969), (3 * sizeof(double)));
    memcpy((output + 964), (work + 2991), (9 * sizeof(double)));
    output[973] = work[746];
    memcpy((output + 974), (work + 747), (9 * sizeof(double)));
    memcpy((output + 983), (work + 3000), (3 * sizeof(double)));
    memcpy((output + 986), (work + 3022), (9 * sizeof(double)));
    output[995] = work[933];
    memcpy((output + 996), (work + 934), (9 * sizeof(double)));
    memcpy((output + 1005), (work + 3031), (3 * sizeof(double)));
    memcpy((output + 1008), (work + 3053), (9 * sizeof(double)));
    output[1017] = work[1120];
    memcpy((output + 1018), (work + 1121), (9 * sizeof(double)));
    memcpy((output + 1027), (work + 3062), (3 * sizeof(double)));
    memcpy((output + 1030), (work + 3084), (9 * sizeof(double)));
    output[1039] = work[1433];
    memcpy((output + 1040), (work + 1434), (9 * sizeof(double)));
    memcpy((output + 1049), (work + 3093), (3 * sizeof(double)));
    memcpy((output + 1052), (work + 3115), (9 * sizeof(double)));
    output[1061] = work[1620];
    memcpy((output + 1062), (work + 1621), (9 * sizeof(double)));
    memcpy((output + 1071), (work + 3124), (3 * sizeof(double)));
    memcpy((output + 1074), (work + 3146), (9 * sizeof(double)));
    output[1083] = work[1807];
    memcpy((output + 1084), (work + 1808), (9 * sizeof(double)));
    memcpy((output + 1093), (work + 3155), (3 * sizeof(double)));
    memcpy((output + 1096), (work + 3177), (9 * sizeof(double)));
    output[1105] = work[1994];
    memcpy((output + 1106), (work + 1995), (9 * sizeof(double)));
    memcpy((output + 1115), (work + 3186), (3 * sizeof(double)));
    memcpy((output + 1118), (work + 3208), (9 * sizeof(double)));
    output[1127] = work[2181];
    memcpy((output + 1128), (work + 2182), (9 * sizeof(double)));
    memcpy((output + 1137), (work + 3217), (3 * sizeof(double)));
    memcpy((output + 1140), (work + 3239), (9 * sizeof(double)));
    output[1149] = work[2368];
    memcpy((output + 1150), (work + 2369), (9 * sizeof(double)));
    memcpy((output + 1159), (work + 3248), (3 * sizeof(double)));
    memcpy((output + 1162), (work + 3270), (9 * sizeof(double)));
    output[1171] = work[2597];
    memcpy((output + 1172), (work + 2598), (9 * sizeof(double)));
    memcpy((output + 1181), (work + 3279), (3 * sizeof(double)));
    memcpy((output + 1184), (work + 3301), (9 * sizeof(double)));
    output[1193] = work[2742];
    memcpy((output + 1194), (work + 2743), (9 * sizeof(double)));
    memcpy((output + 1203), (work + 3310), (3 * sizeof(double)));
    memcpy((output + 1206), (work + 3332), (9 * sizeof(double)));
    output[1215] = work[3341];
    output[1216] = work[3342];
    output[1217] = work[3343];
    memcpy((output + 1218), (work + 1307), (3 * sizeof(double)));
    memcpy((output + 1221), (work + 3344), (3 * sizeof(double)));
    memcpy((output + 1224), (work + 2761), (3 * sizeof(double)));
    output[1227] = work[3347];
    output[1228] = work[3348];
    output[1229] = work[3349];
    memcpy((output + 1230), (work + 517), (3 * sizeof(double)));
    memcpy((output + 1233), (work + 3350), (3 * sizeof(double)));
    memcpy((output + 1236), (work + 2773), (3 * sizeof(double)));
    output[1239] = work[3353];
    output[1240] = work[3354];
    output[1241] = work[3355];
    memcpy((output + 1242), (work + 1349), (3 * sizeof(double)));
    memcpy((output + 1245), (work + 3356), (3 * sizeof(double)));
    memcpy((output + 1248), (work + 2777), (3 * sizeof(double)));
    output[1251] = work[3359];
    output[1252] = work[3360];
    output[1253] = work[3361];
    memcpy((output + 1254), (work + 1265), (3 * sizeof(double)));
    memcpy((output + 1257), (work + 3362), (3 * sizeof(double)));
    memcpy((output + 1260), (work + 2781), (3 * sizeof(double)));
    output[1263] = work[3365];
    output[1264] = work[3366];
    output[1265] = work[3367];
    memcpy((output + 1266), (work + 1078), (3 * sizeof(double)));
    memcpy((output + 1269), (work + 3368), (3 * sizeof(double)));
    memcpy((output + 1272), (work + 2793), (3 * sizeof(double)));
    output[1275] = work[3371];
    output[1276] = work[3372];
    output[1277] = work[3373];
    memcpy((output + 1278), (work + 1391), (3 * sizeof(double)));
    memcpy((output + 1281), (work + 3374), (3 * sizeof(double)));
    memcpy((output + 1284), (work + 2797), (3 * sizeof(double)));
    output[1287] = work[3377];
    output[1288] = work[3378];
    output[1289] = work[3379];
    memcpy((output + 1290), (work + 1578), (3 * sizeof(double)));
    memcpy((output + 1293), (work + 3380), (3 * sizeof(double)));
    memcpy((output + 1296), (work + 2801), (3 * sizeof(double)));
    output[1299] = work[3383];
    output[1300] = work[3384];
    output[1301] = work[3385];
    memcpy((output + 1302), (work + 1723), (3 * sizeof(double)));
    memcpy((output + 1305), (work + 3386), (3 * sizeof(double)));
    memcpy((output + 1308), (work + 2805), (3 * sizeof(double)));
    output[1311] = work[3389];
    output[1312] = work[3390];
    output[1313] = work[3391];
    memcpy((output + 1314), (work + 1910), (3 * sizeof(double)));
    memcpy((output + 1317), (work + 3392), (3 * sizeof(double)));
    memcpy((output + 1320), (work + 2809), (3 * sizeof(double)));
    output[1323] = work[3395];
    output[1324] = work[3396];
    output[1325] = work[3397];
    memcpy((output + 1326), (work + 2139), (3 * sizeof(double)));
    memcpy((output + 1329), (work + 3398), (3 * sizeof(double)));
    memcpy((output + 1332), (work + 2813), (3 * sizeof(double)));
    output[1335] = work[3401];
    output[1336] = work[3402];
    output[1337] = work[3403];
    memcpy((output + 1338), (work + 2513), (3 * sizeof(double)));
    memcpy((output + 1341), (work + 3404), (3 * sizeof(double)));
    memcpy((output + 1344), (work + 2817), (3 * sizeof(double)));
    output[1347] = work[3407];
    output[1348] = work[3408];
    output[1349] = work[3409];
    memcpy((output + 1350), (work + 2870), (3 * sizeof(double)));
    memcpy((output + 1353), (work + 3410), (3 * sizeof(double)));
    output[1356] = work[3413];
    output[1357] = work[3414];
    output[1358] = work[3415];
    memcpy((output + 1359), (work + 2284), (3 * sizeof(double)));
    memcpy((output + 1362), (work + 3416), (3 * sizeof(double)));
    output[1365] = work[3419];
    output[1366] = work[3420];
    output[1367] = work[3421];
    memcpy((output + 1368), (work + 2555), (3 * sizeof(double)));
    memcpy((output + 1371), (work + 3422), (3 * sizeof(double)));
    output[1374] = work[3425];
    output[1375] = work[3426];
    output[1376] = work[3427];
    memcpy((output + 1377), (work + 3428), (3 * sizeof(double)));
    memcpy((output + 1380), (work + 3431), (3 * sizeof(double)));
    memcpy((output + 1383), (work + 2785), (3 * sizeof(double)));
    memcpy((output + 1386), (work + 2789), (3 * sizeof(double)));
    memcpy((output + 1389), (work + 3434), (2 * sizeof(double)));
    memcpy((output + 1391), (work + 3436), (2 * sizeof(double)));
    memcpy((output + 1393), (work + 3438), (2 * sizeof(double)));
    memcpy((output + 1395), (work + 3442), (3 * sizeof(double)));
    memcpy((output + 1398), (work + 3445), (3 * sizeof(double)));
    memcpy((output + 1401), (work + 2765), (3 * sizeof(double)));
    memcpy((output + 1404), (work + 2769), (3 * sizeof(double)));
    memcpy((output + 1407), (work + 3448), (2 * sizeof(double)));
    memcpy((output + 1409), (work + 3450), (2 * sizeof(double)));
    memcpy((output + 1411), (work + 3452), (2 * sizeof(double)));
    memcpy((output + 1413), (work + 3456), (9 * sizeof(double)));
EXIT_POINT:
    (void)msg;
    (void)msg_size;
    return error;
}
