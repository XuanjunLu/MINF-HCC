import numpy
from six.moves import range
import scipy.io as sio
import SimpleITK as sitk
from PIL import Image
import numpy as np
import skimage
from skimage import measure
from skimage import morphology
import pandas as pd
from pathomics import base
# from .matlab import *
import os
from .flock_extractor.flock_feat_extractor import flock_feat_extractor


class PathomicsFLocK(base.PathomicsFeaturesBase):

    def __init__(self, inputImage, inputMask, **kwargs):
        super(PathomicsFLocK, self).__init__(inputImage, inputMask, **kwargs)
        self.name = 'FLocK'
        self.image = sitk.GetArrayViewFromImage(self.inputImage)
        self.mask = sitk.GetArrayViewFromImage(self.inputMask)
        if len(self.mask.shape) > 2:
            self.mask = self.mask[:, :, 0]
        self.bounds, self.image_intensity, self.feats = self.mask2bounds(
            self.mask, self.image, atts=['area'], **kwargs)
        self.features, _ = flock_feat_extractor(self.image_intensity,
                                                np.array(self.feats),
                                                ifShowFig=False,
                                                bandwidth=150)      # 180
        
    def getOutIntersectAbsAreaMinFeatureValue(self):
        return self.features[0]

    def getOutIntersectAbsAreaMaxFeatureValue(self):
        return self.features[1]

    def getOutIntersectAbsAreaRangeFeatureValue(self):
        return self.features[2]

    def getOutIntersectAbsAreaMeanFeatureValue(self):
        return self.features[3]

    def getOutIntersectAbsAreaMedianFeatureValue(self):
        return self.features[4]

    def getOutIntersectAbsAreaStdFeatureValue(self):
        return self.features[5]

    def getOutIntersectAbsAreaKurtosisFeatureValue(self):
        return self.features[6]

    def getOutIntersectAbsAreaSkewnessFeatureValue(self):
        return self.features[7]

    def getOutIntersectCountTotalIntersectFeatureValue(self):
        return self.features[8]

    def getOutIntersectCountPortionIntersectedFeatureValue(self):
        return self.features[9]

    def getOutIntersectMaxIntersectAreaCountSum01FeatureValue(self):
        return self.features[10]

    def getOutIntersectMaxIntersectAreaCountSum02FeatureValue(self):
        return self.features[11]

    def getOutIntersectMaxIntersectAreaCountSum03FeatureValue(self):
        return self.features[12]

    def getOutIntersectMaxIntersectAreaOverClustSum01FeatureValue(self):
        return self.features[13]

    def getOutIntersectMaxIntersectAreaOverClustSum02FeatureValue(self):
        return self.features[14]

    def getOutIntersectMaxIntersectAreaOverClustSum03FeatureValue(self):
        return self.features[15]

    def getOutIntersectMinIntersectAreaStatMinFeatureValue(self):
        return self.features[16]

    def getOutIntersectMinIntersectAreaStatMaxFeatureValue(self):
        return self.features[17]

    def getOutIntersectMinIntersectAreaStatRangeFeatureValue(self):
        return self.features[18]

    def getOutIntersectMinIntersectAreaStatMeanFeatureValue(self):
        return self.features[19]

    def getOutIntersectMinIntersectAreaStatMedianFeatureValue(self):
        return self.features[20]

    def getOutIntersectMinIntersectAreaStatStdFeatureValue(self):
        return self.features[21]

    def getOutIntersectMinIntersectAreaStatKurtosisFeatureValue(self):
        return self.features[22]

    def getOutIntersectMinIntersectAreaStatSkewnessFeatureValue(self):
        return self.features[23]

    def getOutSpatialIntersectVoronoiAreaStdFeatureValue(self):
        return self.features[24]

    def getOutSpatialIntersectVoronoiAreaMeanFeatureValue(self):
        return self.features[25]

    def getOutSpatialIntersectVoronoiAreaMinMaxFeatureValue(self):
        return self.features[26]

    def getOutSpatialIntersectVoronoiAreaDisorderFeatureValue(self):
        return self.features[27]

    def getOutSpatialIntersectVoronoiPeriStdFeatureValue(self):
        return self.features[28]

    def getOutSpatialIntersectVoronoiPeriMeanFeatureValue(self):
        return self.features[29]

    def getOutSpatialIntersectVoronoiPeriMinMaxFeatureValue(self):
        return self.features[30]

    def getOutSpatialIntersectVoronoiPeriDisorderFeatureValue(self):
        return self.features[31]

    def getOutSpatialIntersectVoronoiChordStdFeatureValue(self):
        return self.features[32]

    def getOutSpatialIntersectVoronoiChordMeanFeatureValue(self):
        return self.features[33]

    def getOutSpatialIntersectVoronoiChordMinMaxFeatureValue(self):
        return self.features[34]

    def getOutSpatialIntersectVoronoiChordDisorderFeatureValue(self):
        return self.features[35]

    def getOutSpatialIntersectDelaunayPeriMinMaxFeatureValue(self):
        return self.features[36]

    def getOutSpatialIntersectDelaunayPeriStdFeatureValue(self):
        return self.features[37]

    def getOutSpatialIntersectDelaunayPeriMeanFeatureValue(self):
        return self.features[38]

    def getOutSpatialIntersectDelaunayPeriDisorderFeatureValue(self):
        return self.features[39]

    def getOutSpatialIntersectDelaunayAreaMinMaxFeatureValue(self):
        return self.features[40]

    def getOutSpatialIntersectDelaunayAreaStdFeatureValue(self):
        return self.features[41]

    def getOutSpatialIntersectDelaunayAreaMeanFeatureValue(self):
        return self.features[42]

    def getOutSpatialIntersectDelaunayAreaDisorderFeatureValue(self):
        return self.features[43]

    def getOutSpatialIntersectMstEdgeMeanFeatureValue(self):
        return self.features[44]

    def getOutSpatialIntersectMstEdgeStdFeatureValue(self):
        return self.features[45]

    def getOutSpatialIntersectMstEdgeMinMaxFeatureValue(self):
        return self.features[46]

    def getOutSpatialIntersectMstEdgeDisorderFeatureValue(self):
        return self.features[47]

    def getOutSpatialIntersectNucSumFeatureValue(self):
        return self.features[48]

    def getOutSpatialIntersectNucVorAreaFeatureValue(self):
        return self.features[49]

    def getOutSpatialIntersectNucDensityFeatureValue(self):
        return self.features[50]

    def getOutSpatialIntersectKnnStd3FeatureValue(self):
        return self.features[51]

    def getOutSpatialIntersectKnnMean3FeatureValue(self):
        return self.features[52]

    def getOutSpatialIntersectKnnDisorder3FeatureValue(self):
        return self.features[53]

    def getOutSpatialIntersectKnnStd5FeatureValue(self):
        return self.features[54]

    def getOutSpatialIntersectKnnMean5FeatureValue(self):
        return self.features[55]

    def getOutSpatialIntersectKnnDisorder5FeatureValue(self):
        return self.features[56]

    def getOutSpatialIntersectKnnStd7FeatureValue(self):
        return self.features[57]

    def getOutSpatialIntersectKnnMean7FeatureValue(self):
        return self.features[58]

    def getOutSpatialIntersectKnnDisorder7FeatureValue(self):
        return self.features[59]

    def getOutSpatialIntersectRrStd10FeatureValue(self):
        return self.features[60]

    def getOutSpatialIntersectRrMean10FeatureValue(self):
        return self.features[61]

    def getOutSpatialIntersectRrDisorder10FeatureValue(self):
        return self.features[62]

    def getOutSpatialIntersectRrStd20FeatureValue(self):
        return self.features[63]

    def getOutSpatialIntersectRrMean20FeatureValue(self):
        return self.features[64]

    def getOutSpatialIntersectRrDisorder20FeatureValue(self):
        return self.features[65]

    def getOutSpatialIntersectRrStd30FeatureValue(self):
        return self.features[66]

    def getOutSpatialIntersectRrMean30FeatureValue(self):
        return self.features[67]

    def getOutSpatialIntersectRrDisorder30FeatureValue(self):
        return self.features[68]

    def getOutSpatialIntersectRrStd40FeatureValue(self):
        return self.features[69]

    def getOutSpatialIntersectRrMean40FeatureValue(self):
        return self.features[70]

    def getOutSpatialIntersectRrDisorder40FeatureValue(self):
        return self.features[71]

    def getOutSpatialIntersectRrStd50FeatureValue(self):
        return self.features[72]

    def getOutSpatialIntersectRrMean50FeatureValue(self):
        return self.features[73]

    def getOutSpatialIntersectRrDisorder50FeatureValue(self):
        return self.features[74]

    def getOutSpatialClusterVoronoiAreaStdFeatureValue(self):
        return self.features[75]

    def getOutSpatialClusterVoronoiAreaMeanFeatureValue(self):
        return self.features[76]

    def getOutSpatialClusterVoronoiAreaMinMaxFeatureValue(self):
        return self.features[77]

    def getOutSpatialClusterVoronoiAreaDisorderFeatureValue(self):
        return self.features[78]

    def getOutSpatialClusterVoronoiPeriStdFeatureValue(self):
        return self.features[79]

    def getOutSpatialClusterVoronoiPeriMeanFeatureValue(self):
        return self.features[80]

    def getOutSpatialClusterVoronoiPeriMinMaxFeatureValue(self):
        return self.features[81]

    def getOutSpatialClusterVoronoiPeriDisorderFeatureValue(self):
        return self.features[82]

    def getOutSpatialClusterVoronoiChordStdFeatureValue(self):
        return self.features[83]

    def getOutSpatialClusterVoronoiChordMeanFeatureValue(self):
        return self.features[84]

    def getOutSpatialClusterVoronoiChordMinMaxFeatureValue(self):
        return self.features[85]

    def getOutSpatialClusterVoronoiChordDisorderFeatureValue(self):
        return self.features[86]

    def getOutSpatialClusterDelaunayPeriMinMaxFeatureValue(self):
        return self.features[87]

    def getOutSpatialClusterDelaunayPeriStdFeatureValue(self):
        return self.features[88]

    def getOutSpatialClusterDelaunayPeriMeanFeatureValue(self):
        return self.features[89]

    def getOutSpatialClusterDelaunayPeriDisorderFeatureValue(self):
        return self.features[90]

    def getOutSpatialClusterDelaunayAreaMinMaxFeatureValue(self):
        return self.features[91]

    def getOutSpatialClusterDelaunayAreaStdFeatureValue(self):
        return self.features[92]

    def getOutSpatialClusterDelaunayAreaMeanFeatureValue(self):
        return self.features[93]

    def getOutSpatialClusterDelaunayAreaDisorderFeatureValue(self):
        return self.features[94]

    def getOutSpatialClusterMstEdgeMeanFeatureValue(self):
        return self.features[95]

    def getOutSpatialClusterMstEdgeStdFeatureValue(self):
        return self.features[96]

    def getOutSpatialClusterMstEdgeMinMaxFeatureValue(self):
        return self.features[97]

    def getOutSpatialClusterMstEdgeDisorderFeatureValue(self):
        return self.features[98]

    def getOutSpatialClusterNucSumFeatureValue(self):
        return self.features[99]

    def getOutSpatialClusterNucVorAreaFeatureValue(self):
        return self.features[100]

    def getOutSpatialClusterNucDensityFeatureValue(self):
        return self.features[101]

    def getOutSpatialClusterKnnStd3FeatureValue(self):
        return self.features[102]

    def getOutSpatialClusterKnnMean3FeatureValue(self):
        return self.features[103]

    def getOutSpatialClusterKnnDisorder3FeatureValue(self):
        return self.features[104]

    def getOutSpatialClusterKnnStd5FeatureValue(self):
        return self.features[105]

    def getOutSpatialClusterKnnMean5FeatureValue(self):
        return self.features[106]

    def getOutSpatialClusterKnnDisorder5FeatureValue(self):
        return self.features[107]

    def getOutSpatialClusterKnnStd7FeatureValue(self):
        return self.features[108]

    def getOutSpatialClusterKnnMean7FeatureValue(self):
        return self.features[109]

    def getOutSpatialClusterKnnDisorder7FeatureValue(self):
        return self.features[110]

    def getOutSpatialClusterRrStd10FeatureValue(self):
        return self.features[111]

    def getOutSpatialClusterRrMean10FeatureValue(self):
        return self.features[112]

    def getOutSpatialClusterRrDisorder10FeatureValue(self):
        return self.features[113]

    def getOutSpatialClusterRrStd20FeatureValue(self):
        return self.features[114]

    def getOutSpatialClusterRrMean20FeatureValue(self):
        return self.features[115]

    def getOutSpatialClusterRrDisorder20FeatureValue(self):
        return self.features[116]

    def getOutSpatialClusterRrStd30FeatureValue(self):
        return self.features[117]

    def getOutSpatialClusterRrMean30FeatureValue(self):
        return self.features[118]

    def getOutSpatialClusterRrDisorder30FeatureValue(self):
        return self.features[119]

    def getOutSpatialClusterRrStd40FeatureValue(self):
        return self.features[120]

    def getOutSpatialClusterRrMean40FeatureValue(self):
        return self.features[121]

    def getOutSpatialClusterRrDisorder40FeatureValue(self):
        return self.features[122]

    def getOutSpatialClusterRrStd50FeatureValue(self):
        return self.features[123]

    def getOutSpatialClusterRrMean50FeatureValue(self):
        return self.features[124]

    def getOutSpatialClusterRrDisorder50FeatureValue(self):
        return self.features[125]

    def getOutSizeFlockSizeClusterCountFeatureValue(self):
        return self.features[126]

    def getOutSizeFlockNumNucInClusterMinFeatureValue(self):
        return self.features[127]

    def getOutSizeFlockNumNucInClusterMaxFeatureValue(self):
        return self.features[128]

    def getOutSizeFlockNumNucInClusterRangeFeatureValue(self):
        return self.features[129]

    def getOutSizeFlockNumNucInClusterMeanFeatureValue(self):
        return self.features[130]

    def getOutSizeFlockNumNucInClusterMedianFeatureValue(self):
        return self.features[131]

    def getOutSizeFlockNumNucInClusterStdFeatureValue(self):
        return self.features[132]

    def getOutSizeFlockNumNucInClusterKurtosisFeatureValue(self):
        return self.features[133]

    def getOutSizeFlockNumNucInClusterSkewnessFeatureValue(self):
        return self.features[134]

    def getOutSizeFlockNucDensityOverSizeMinFeatureValue(self):
        return self.features[135]

    def getOutSizeFlockNucDensityOverSizeMaxFeatureValue(self):
        return self.features[136]

    def getOutSizeFlockNucDensityOverSizeRangeFeatureValue(self):
        return self.features[137]

    def getOutSizeFlockNucDensityOverSizeMeanFeatureValue(self):
        return self.features[138]

    def getOutSizeFlockNucDensityOverSizeMedianFeatureValue(self):
        return self.features[139]

    def getOutSizeFlockNucDensityOverSizeStdFeatureValue(self):
        return self.features[140]

    def getOutSizeFlockNucDensityOverSizeKurtosisFeatureValue(self):
        return self.features[141]

    def getOutSizeFlockNucDensityOverSizeSkewnessFeatureValue(self):
        return self.features[142]

    def getOutPolygonFlockOtherAttrMinFeatureValue(self):
        return self.features[143]

    def getOutPolygonFlockOtherAttrMaxFeatureValue(self):
        return self.features[144]

    def getOutPolygonFlockOtherAttrRangeFeatureValue(self):
        return self.features[145]

    def getOutPolygonFlockOtherAttrMeanFeatureValue(self):
        return self.features[146]

    def getOutPolygonFlockOtherAttrMedianFeatureValue(self):
        return self.features[147]

    def getOutPolygonFlockOtherAttrStdFeatureValue(self):
        return self.features[148]

    def getOutPolygonFlockOtherAttrKurtosisFeatureValue(self):
        return self.features[149]

    def getOutPolygonFlockOtherAttrSkewnessFeatureValue(self):
        return self.features[150]

    def getOutPolygonSpanVarDist2ClustCentMinFeatureValue(self):
        return self.features[151]

    def getOutPolygonSpanVarDist2ClustCentMaxFeatureValue(self):
        return self.features[152]

    def getOutPolygonSpanVarDist2ClustCentRangeFeatureValue(self):
        return self.features[153]

    def getOutPolygonSpanVarDist2ClustCentMeanFeatureValue(self):
        return self.features[154]

    def getOutPolygonSpanVarDist2ClustCentMedianFeatureValue(self):
        return self.features[155]

    def getOutPolygonSpanVarDist2ClustCentStdFeatureValue(self):
        return self.features[156]

    def getOutPolygonSpanVarDist2ClustCentKurtosisFeatureValue(self):
        return self.features[157]

    def getOutPolygonSpanVarDist2ClustCentSkewnessFeatureValue(self):
        return self.features[158]

    def getOutPhenotypePhenoEnrichmentMinFeatureValue(self):
        return self.features[159]

    def getOutPhenotypePhenoEnrichmentMaxFeatureValue(self):
        return self.features[160]

    def getOutPhenotypePhenoEnrichmentRangeFeatureValue(self):
        return self.features[161]

    def getOutPhenotypePhenoEnrichmentMeanFeatureValue(self):
        return self.features[162]

    def getOutPhenotypePhenoEnrichmentMedianFeatureValue(self):
        return self.features[163]

    def getOutPhenotypePhenoEnrichmentStdFeatureValue(self):
        return self.features[164]

    def getOutPhenotypePhenoEnrichmentKurtosisFeatureValue(self):
        return self.features[165]

    def getOutPhenotypePhenoEnrichmentSkewnessFeatureValue(self):
        return self.features[166]

    def getOutPhenotypePhenoIntraSameTypeStat0SumFeatureValue(self):
        return self.features[167]

    def getOutPhenotypePhenoIntraSameTypeStat0RatiosumFeatureValue(self):
        return self.features[168]

    def getOutPhenotypePhenoInterDiffTypeStat0SumFeatureValue(self):
        return self.features[169]

    def getOutPhenotypePhenoInterDiffTypeStat0RatiosumFeatureValue(self):
        return self.features[170]

    def getPhenoSpatialGraphByType0VoronoiAreaStdFeatureValue(self):
        return self.features[171]

    def getPhenoSpatialGraphByType0VoronoiAreaMeanFeatureValue(self):
        return self.features[172]

    def getPhenoSpatialGraphByType0VoronoiAreaMinMaxFeatureValue(self):
        return self.features[173]

    def getPhenoSpatialGraphByType0VoronoiAreaDisorderFeatureValue(self):
        return self.features[174]

    def getPhenoSpatialGraphByType0VoronoiPeriStdFeatureValue(self):
        return self.features[175]

    def getPhenoSpatialGraphByType0VoronoiPeriMeanFeatureValue(self):
        return self.features[176]

    def getPhenoSpatialGraphByType0VoronoiPeriMinMaxFeatureValue(self):
        return self.features[177]

    def getPhenoSpatialGraphByType0VoronoiPeriDisorderFeatureValue(self):
        return self.features[178]

    def getPhenoSpatialGraphByType0VoronoiChordStdFeatureValue(self):
        return self.features[179]

    def getPhenoSpatialGraphByType0VoronoiChordMeanFeatureValue(self):
        return self.features[180]

    def getPhenoSpatialGraphByType0VoronoiChordMinMaxFeatureValue(self):
        return self.features[181]

    def getPhenoSpatialGraphByType0VoronoiChordDisorderFeatureValue(self):
        return self.features[182]

    def getPhenoSpatialGraphByType0DelaunayPeriMinMaxFeatureValue(self):
        return self.features[183]

    def getPhenoSpatialGraphByType0DelaunayPeriStdFeatureValue(self):
        return self.features[184]

    def getPhenoSpatialGraphByType0DelaunayPeriMeanFeatureValue(self):
        return self.features[185]

    def getPhenoSpatialGraphByType0DelaunayPeriDisorderFeatureValue(self):
        return self.features[186]

    def getPhenoSpatialGraphByType0DelaunayAreaMinMaxFeatureValue(self):
        return self.features[187]

    def getPhenoSpatialGraphByType0DelaunayAreaStdFeatureValue(self):
        return self.features[188]

    def getPhenoSpatialGraphByType0DelaunayAreaMeanFeatureValue(self):
        return self.features[189]

    def getPhenoSpatialGraphByType0DelaunayAreaDisorderFeatureValue(self):
        return self.features[190]

    def getPhenoSpatialGraphByType0MstEdgeMeanFeatureValue(self):
        return self.features[191]

    def getPhenoSpatialGraphByType0MstEdgeStdFeatureValue(self):
        return self.features[192]

    def getPhenoSpatialGraphByType0MstEdgeMinMaxFeatureValue(self):
        return self.features[193]

    def getPhenoSpatialGraphByType0MstEdgeDisorderFeatureValue(self):
        return self.features[194]

    def getPhenoSpatialGraphByType0NucSumFeatureValue(self):
        return self.features[195]

    def getPhenoSpatialGraphByType0NucVorAreaFeatureValue(self):
        return self.features[196]

    def getPhenoSpatialGraphByType0NucDensityFeatureValue(self):
        return self.features[197]

    def getPhenoSpatialGraphByType0KnnStd3FeatureValue(self):
        return self.features[198]

    def getPhenoSpatialGraphByType0KnnMean3FeatureValue(self):
        return self.features[199]

    def getPhenoSpatialGraphByType0KnnDisorder3FeatureValue(self):
        return self.features[200]

    def getPhenoSpatialGraphByType0KnnStd5FeatureValue(self):
        return self.features[201]

    def getPhenoSpatialGraphByType0KnnMean5FeatureValue(self):
        return self.features[202]

    def getPhenoSpatialGraphByType0KnnDisorder5FeatureValue(self):
        return self.features[203]

    def getPhenoSpatialGraphByType0KnnStd7FeatureValue(self):
        return self.features[204]

    def getPhenoSpatialGraphByType0KnnMean7FeatureValue(self):
        return self.features[205]

    def getPhenoSpatialGraphByType0KnnDisorder7FeatureValue(self):
        return self.features[206]

    def getPhenoSpatialGraphByType0RrStd10FeatureValue(self):
        return self.features[207]

    def getPhenoSpatialGraphByType0RrMean10FeatureValue(self):
        return self.features[208]

    def getPhenoSpatialGraphByType0RrDisorder10FeatureValue(self):
        return self.features[209]

    def getPhenoSpatialGraphByType0RrStd20FeatureValue(self):
        return self.features[210]

    def getPhenoSpatialGraphByType0RrMean20FeatureValue(self):
        return self.features[211]

    def getPhenoSpatialGraphByType0RrDisorder20FeatureValue(self):
        return self.features[212]

    def getPhenoSpatialGraphByType0RrStd30FeatureValue(self):
        return self.features[213]

    def getPhenoSpatialGraphByType0RrMean30FeatureValue(self):
        return self.features[214]

    def getPhenoSpatialGraphByType0RrDisorder30FeatureValue(self):
        return self.features[215]

    def getPhenoSpatialGraphByType0RrStd40FeatureValue(self):
        return self.features[216]

    def getPhenoSpatialGraphByType0RrMean40FeatureValue(self):
        return self.features[217]

    def getPhenoSpatialGraphByType0RrDisorder40FeatureValue(self):
        return self.features[218]

    def getPhenoSpatialGraphByType0RrStd50FeatureValue(self):
        return self.features[219]

    def getPhenoSpatialGraphByType0RrMean50FeatureValue(self):
        return self.features[220]

    def getPhenoSpatialGraphByType0RrDisorder50FeatureValue(self):
        return self.features[221]

