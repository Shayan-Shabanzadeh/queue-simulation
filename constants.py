# LCG parameters
from ApplicationSubmissionQueue import ApplicationSubmissionQueue
from ComplaintsQueue import ComplaintsQueue
from CoreA import CoreA
from CoreB import CoreB
from CoreC import CoreC
from DocumentVerificationQueue import DocumentVerificationQueue
from ReviewRequestQueue import ReviewRequestQueue
from WritingQueue import WritingQueue

seed = 42
# a = 1664525
# c = 1013904223
# m = 2 ** 32
CORE_TYPES = [CoreA, CoreB, CoreC]
QUEUE_TYPES = [WritingQueue, ComplaintsQueue, DocumentVerificationQueue, ApplicationSubmissionQueue, ReviewRequestQueue]
