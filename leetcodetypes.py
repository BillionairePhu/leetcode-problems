from typing import Any, List, Optional
from pydantic import BaseModel

class Contributor(BaseModel):
    username: str
    profileUrl: str
    avatarUrl: str


class TopicTag(BaseModel):
    name: str
    slug: str
    translatedName: Optional[str]
    id: Optional[str]


class CodeSnippet(BaseModel):
    lang: str
    langSlug: str
    code: str


class Solution(BaseModel):
    id: str
    canSeeDetail: bool
    paidOnly: bool
    hasVideoSolution: bool
    paidOnlyVideo: bool


class ChallengeQuestion(BaseModel):
    id: str
    date: str
    incompleteChallengeCount: int
    streakCount: int
    type: str

class Questionling(BaseModel):
    acRate: float
    difficulty: str
    freqBar: Optional[float]
    questionFrontendId: str
    title: str
    titleSlug: str
    topicTags: List[TopicTag]
    solution: Optional[Solution]

class Question(Questionling):
    questionId: str
    content: str
    translatedTitle: Optional[str]
    translatedContent: Optional[str]
    isPaidOnly: bool
    boundTopicId: Optional[int]
    likes: int
    dislikes: int
    isLiked: Optional[bool]
    isFavor: Optional[bool]
    similarQuestions: Optional[str]
    exampleTestcases: str
    contributors: List[Contributor]
    companyTagStats: Optional[Any]
    codeSnippets: List[CodeSnippet]
    stats: str
    hints: List[str]
    status: Optional[str]
    sampleTestCase: str
    metaData: str
    judgerAvailable: bool
    judgeType: str
    mysqlSchemas: Optional[Any]
    enableRunCode: bool
    enableTestMode: bool
    enableDebugger: bool
    envInfo: str
    libraryUrl: Optional[str]
    adminUrl: Optional[str]
    challengeQuestion: Optional[ChallengeQuestion]
    note: Optional[str]


class ActiveDailyCodingChallengeQuestion(BaseModel):
    date: str
    link: str
    question: Question

class ProblemSetQuestionList(BaseModel):
    total: int
    questions: List[Questionling]