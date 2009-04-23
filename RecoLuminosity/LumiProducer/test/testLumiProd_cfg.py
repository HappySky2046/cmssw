
import FWCore.ParameterSet.Config as cms

process = cms.Process("standalonetest")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.load("RecoLuminosity.LumiProducer.nonGlobalTagLumiProducerPrep_cff")

import FWCore.Framework.test.cmsExceptionsFatalOption_cff
process.options = cms.untracked.PSet(
#  wantSummary = cms.untracked.bool(True),
  Rethrow = FWCore.Framework.test.cmsExceptionsFatalOption_cff.Rethrow
)

process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(3)
)

process.source = cms.Source("EmptyIOVSource",
    timetype = cms.string('lumiid'),
    firstValue = cms.uint64(42949672962),
    lastValue = cms.uint64(42949672964),
    interval = cms.uint64(1)
)

process.LumiESSource.DBParameters.authenticationPath=cms.untracked.string('/afs/cern.ch/cms/DB/conddb')
process.LumiESSource.toGet=cms.VPSet(cms.PSet(
    record = cms.string('LuminosityInfoRcd'),
    tag = cms.string('lumitest')
    ))

process.lumiProducer=cms.EDProducer("LumiProducer")
process.test = cms.EDAnalyzer("TestLumiProducer")

process.out = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string('testLumiProd.root')
)

process.p1 = cms.Path(process.lumiProducer * process.test)

process.e = cms.EndPath(process.out)
