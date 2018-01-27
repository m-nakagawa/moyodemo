<?xml version="1.0" ?>
<map version="1.0.1">
    <!--FreeMindフォーマットです-->
    <node ID="ID_123" TEXT="Test9.sparql">
        <node ID="ID_124" POSITION="right" TEXT="root">
            <node ID="ID_125" TEXT="query(QueryContext)">
                <node ID="ID_126" TEXT="prologue(PrologueContext)">
                    <node ID="ID_127" TEXT="prefixDecl(PrefixDeclContext)">
                        <node ID="ID_128" TEXT="PREFIX"/>
                        <node ID="ID_129" TEXT=":"/>
                        <node ID="ID_130" TEXT="&lt;http://bizar.aitc.jp/ns/fos/0.1/&gt;"/>
                    </node>
                    <node ID="ID_131" TEXT="prefixDecl(PrefixDeclContext)">
                        <node ID="ID_132" TEXT="PREFIX"/>
                        <node ID="ID_133" TEXT="ha:"/>
                        <node ID="ID_134" TEXT="&lt;http://bizar.aitc.jp/ns/fos/0.1/人間API/&gt;"/>
                    </node>
                </node>
                <node ID="ID_135" TEXT="selectQuery(SelectQueryContext)">
                    <node ID="ID_136" TEXT="selectClause(SelectClauseContext)">
                        <node ID="ID_137" TEXT="SELECT"/>
                        <node ID="ID_138" TEXT="selectVariables(SelectVariablesContext)">
                            <node ID="ID_139" TEXT="var(VarContext)">
                                <node ID="ID_140" TEXT="?x"/>
                            </node>
                        </node>
                        <node ID="ID_141" TEXT="selectVariables(SelectVariablesContext)">
                            <node ID="ID_142" TEXT="var(VarContext)">
                                <node ID="ID_143" TEXT="?url"/>
                            </node>
                        </node>
                    </node>
                    <node ID="ID_144" TEXT="whereClause(WhereClauseContext)">
                        <node ID="ID_145" TEXT="WHERE"/>
                        <node ID="ID_146" TEXT="groupGraphPattern(GroupGraphPatternContext)">
                            <node ID="ID_147" TEXT="{"/>
                            <node ID="ID_148" TEXT="groupGraphPatternSub(GroupGraphPatternSubContext)">
                                <node ID="ID_149" TEXT="groupGraphPatternSubList(GroupGraphPatternSubListContext)">
                                    <node ID="ID_150" TEXT="graphPatternNotTriples(GraphPatternNotTriplesContext)">
                                        <node ID="ID_151" TEXT="groupOrUnionGraphPattern(GroupOrUnionGraphPatternContext)">
                                            <node ID="ID_152" TEXT="groupGraphPattern(GroupGraphPatternContext)">
                                                <node ID="ID_153" TEXT="{"/>
                                                <node ID="ID_154" TEXT="subSelect(SubSelectContext)">
                                                    <node ID="ID_155" TEXT="selectClause(SelectClauseContext)">
                                                        <node ID="ID_156" TEXT="SELECT"/>
                                                        <node ID="ID_157" TEXT="selectVariables(SelectVariablesContext)">
                                                            <node ID="ID_158" TEXT="var(VarContext)">
                                                                <node ID="ID_159" TEXT="?url"/>
                                                            </node>
                                                        </node>
                                                    </node>
                                                    <node ID="ID_160" TEXT="whereClause(WhereClauseContext)">
                                                        <node ID="ID_161" TEXT="WHERE"/>
                                                        <node ID="ID_162" TEXT="groupGraphPattern(GroupGraphPatternContext)">
                                                            <node ID="ID_163" TEXT="{"/>
                                                            <node ID="ID_164" TEXT="groupGraphPatternSub(GroupGraphPatternSubContext)">
                                                                <node ID="ID_165" TEXT="triplesBlock(TriplesBlockContext)">
                                                                    <node ID="ID_166" TEXT="triplesSameSubjectPath(TriplesSameSubjectPathContext)">
                                                                        <node ID="ID_167" TEXT="varOrTerm(VarOrTermContext)">
                                                                            <node ID="ID_168" TEXT="var(VarContext)">
                                                                                <node ID="ID_169" TEXT="?room"/>
                                                                            </node>
                                                                        </node>
                                                                        <node ID="ID_170" TEXT="propertyListPathNotEmpty(PropertyListPathNotEmptyContext)">
                                                                            <node ID="ID_171" TEXT="verbPath(VerbPathContext)">
                                                                                <node ID="ID_172" TEXT="path(PathContext)">
                                                                                    <node ID="ID_173" TEXT="pathAlternative(PathAlternativeContext)">
                                                                                        <node ID="ID_174" TEXT="pathSequence(PathSequenceContext)">
                                                                                            <node ID="ID_175" TEXT="pathEltOrInverse(PathEltOrInverseContext)">
                                                                                                <node ID="ID_176" TEXT="pathElt(PathEltContext)">
                                                                                                    <node ID="ID_177" TEXT="pathPrimary(PathPrimaryContext)">
                                                                                                        <node ID="ID_178" TEXT="iri(IriContext)">
                                                                                                            <node ID="ID_179" TEXT="prefixedName(PrefixedNameContext)">
                                                                                                                <node ID="ID_180" TEXT=":場所"/>
                                                                                                            </node>
                                                                                                        </node>
                                                                                                    </node>
                                                                                                </node>
                                                                                            </node>
                                                                                        </node>
                                                                                    </node>
                                                                                </node>
                                                                            </node>
                                                                            <node ID="ID_181" TEXT="objectListPath(ObjectListPathContext)">
                                                                                <node ID="ID_182" TEXT="objectPath(ObjectPathContext)">
                                                                                    <node ID="ID_183" TEXT="graphNodePath(GraphNodePathContext)">
                                                                                        <node ID="ID_184" TEXT="varOrTerm(VarOrTermContext)">
                                                                                            <node ID="ID_185" TEXT="graphTerm(GraphTermContext)">
                                                                                                <node ID="ID_186" TEXT="iri(IriContext)">
                                                                                                    <node ID="ID_187" TEXT="prefixedName(PrefixedNameContext)">
                                                                                                        <node ID="ID_188" TEXT=":ここ"/>
                                                                                                    </node>
                                                                                                </node>
                                                                                            </node>
                                                                                        </node>
                                                                                    </node>
                                                                                </node>
                                                                            </node>
                                                                        </node>
                                                                    </node>
                                                                    <node ID="ID_189" TEXT="."/>
                                                                    <node ID="ID_190" TEXT="triplesSameSubjectPath(TriplesSameSubjectPathContext)">
                                                                        <node ID="ID_191" TEXT="varOrTerm(VarOrTermContext)">
                                                                            <node ID="ID_192" TEXT="var(VarContext)">
                                                                                <node ID="ID_193" TEXT="?room"/>
                                                                            </node>
                                                                        </node>
                                                                        <node ID="ID_194" TEXT="propertyListPathNotEmpty(PropertyListPathNotEmptyContext)">
                                                                            <node ID="ID_195" TEXT="verbPath(VerbPathContext)">
                                                                                <node ID="ID_196" TEXT="path(PathContext)">
                                                                                    <node ID="ID_197" TEXT="pathAlternative(PathAlternativeContext)">
                                                                                        <node ID="ID_198" TEXT="pathSequence(PathSequenceContext)">
                                                                                            <node ID="ID_199" TEXT="pathEltOrInverse(PathEltOrInverseContext)">
                                                                                                <node ID="ID_200" TEXT="pathElt(PathEltContext)">
                                                                                                    <node ID="ID_201" TEXT="pathPrimary(PathPrimaryContext)">
                                                                                                        <node ID="ID_202" TEXT="iri(IriContext)">
                                                                                                            <node ID="ID_203" TEXT="prefixedName(PrefixedNameContext)">
                                                                                                                <node ID="ID_204" TEXT=":在室"/>
                                                                                                            </node>
                                                                                                        </node>
                                                                                                    </node>
                                                                                                </node>
                                                                                            </node>
                                                                                        </node>
                                                                                    </node>
                                                                                </node>
                                                                            </node>
                                                                            <node ID="ID_205" TEXT="objectListPath(ObjectListPathContext)">
                                                                                <node ID="ID_206" TEXT="objectPath(ObjectPathContext)">
                                                                                    <node ID="ID_207" TEXT="graphNodePath(GraphNodePathContext)">
                                                                                        <node ID="ID_208" TEXT="varOrTerm(VarOrTermContext)">
                                                                                            <node ID="ID_209" TEXT="var(VarContext)">
                                                                                                <node ID="ID_210" TEXT="?p"/>
                                                                                            </node>
                                                                                        </node>
                                                                                    </node>
                                                                                </node>
                                                                            </node>
                                                                        </node>
                                                                    </node>
                                                                    <node ID="ID_211" TEXT="."/>
                                                                    <node ID="ID_212" TEXT="triplesSameSubjectPath(TriplesSameSubjectPathContext)">
                                                                        <node ID="ID_213" TEXT="varOrTerm(VarOrTermContext)">
                                                                            <node ID="ID_214" TEXT="var(VarContext)">
                                                                                <node ID="ID_215" TEXT="?c"/>
                                                                            </node>
                                                                        </node>
                                                                        <node ID="ID_216" TEXT="propertyListPathNotEmpty(PropertyListPathNotEmptyContext)">
                                                                            <node ID="ID_217" TEXT="verbPath(VerbPathContext)">
                                                                                <node ID="ID_218" TEXT="path(PathContext)">
                                                                                    <node ID="ID_219" TEXT="pathAlternative(PathAlternativeContext)">
                                                                                        <node ID="ID_220" TEXT="pathSequence(PathSequenceContext)">
                                                                                            <node ID="ID_221" TEXT="pathEltOrInverse(PathEltOrInverseContext)">
                                                                                                <node ID="ID_222" TEXT="pathElt(PathEltContext)">
                                                                                                    <node ID="ID_223" TEXT="pathPrimary(PathPrimaryContext)">
                                                                                                        <node ID="ID_224" TEXT="iri(IriContext)">
                                                                                                            <node ID="ID_225" TEXT="prefixedName(PrefixedNameContext)">
                                                                                                                <node ID="ID_226" TEXT=":主人"/>
                                                                                                            </node>
                                                                                                        </node>
                                                                                                    </node>
                                                                                                </node>
                                                                                            </node>
                                                                                        </node>
                                                                                    </node>
                                                                                </node>
                                                                            </node>
                                                                            <node ID="ID_227" TEXT="objectListPath(ObjectListPathContext)">
                                                                                <node ID="ID_228" TEXT="objectPath(ObjectPathContext)">
                                                                                    <node ID="ID_229" TEXT="graphNodePath(GraphNodePathContext)">
                                                                                        <node ID="ID_230" TEXT="varOrTerm(VarOrTermContext)">
                                                                                            <node ID="ID_231" TEXT="var(VarContext)">
                                                                                                <node ID="ID_232" TEXT="?p"/>
                                                                                            </node>
                                                                                        </node>
                                                                                    </node>
                                                                                </node>
                                                                            </node>
                                                                        </node>
                                                                    </node>
                                                                    <node ID="ID_233" TEXT="."/>
                                                                    <node ID="ID_234" TEXT="triplesSameSubjectPath(TriplesSameSubjectPathContext)">
                                                                        <node ID="ID_235" TEXT="varOrTerm(VarOrTermContext)">
                                                                            <node ID="ID_236" TEXT="var(VarContext)">
                                                                                <node ID="ID_237" TEXT="?c"/>
                                                                            </node>
                                                                        </node>
                                                                        <node ID="ID_238" TEXT="propertyListPathNotEmpty(PropertyListPathNotEmptyContext)">
                                                                            <node ID="ID_239" TEXT="verbPath(VerbPathContext)">
                                                                                <node ID="ID_240" TEXT="path(PathContext)">
                                                                                    <node ID="ID_241" TEXT="pathAlternative(PathAlternativeContext)">
                                                                                        <node ID="ID_242" TEXT="pathSequence(PathSequenceContext)">
                                                                                            <node ID="ID_243" TEXT="pathEltOrInverse(PathEltOrInverseContext)">
                                                                                                <node ID="ID_244" TEXT="pathElt(PathEltContext)">
                                                                                                    <node ID="ID_245" TEXT="pathPrimary(PathPrimaryContext)">
                                                                                                        <node ID="ID_246" TEXT="iri(IriContext)">
                                                                                                            <node ID="ID_247" TEXT="prefixedName(PrefixedNameContext)">
                                                                                                                <node ID="ID_248" TEXT="ha:テキストメッセージ"/>
                                                                                                            </node>
                                                                                                        </node>
                                                                                                    </node>
                                                                                                </node>
                                                                                            </node>
                                                                                        </node>
                                                                                    </node>
                                                                                </node>
                                                                            </node>
                                                                            <node ID="ID_249" TEXT="objectListPath(ObjectListPathContext)">
                                                                                <node ID="ID_250" TEXT="objectPath(ObjectPathContext)">
                                                                                    <node ID="ID_251" TEXT="graphNodePath(GraphNodePathContext)">
                                                                                        <node ID="ID_252" TEXT="varOrTerm(VarOrTermContext)">
                                                                                            <node ID="ID_253" TEXT="var(VarContext)">
                                                                                                <node ID="ID_254" TEXT="?url"/>
                                                                                            </node>
                                                                                        </node>
                                                                                    </node>
                                                                                </node>
                                                                            </node>
                                                                        </node>
                                                                    </node>
                                                                    <node ID="ID_255" TEXT="."/>
                                                                </node>
                                                            </node>
                                                            <node ID="ID_256" TEXT="}"/>
                                                        </node>
                                                    </node>
                                                    <node ID="ID_257" TEXT="solutionModifier(SolutionModifierContext)"/>
                                                    <node ID="ID_258" TEXT="valuesClause(ValuesClauseContext)"/>
                                                </node>
                                                <node ID="ID_259" TEXT="}"/>
                                            </node>
                                        </node>
                                    </node>
                                    <node ID="ID_260" TEXT="triplesBlock(TriplesBlockContext)">
                                        <node ID="ID_261" TEXT="triplesSameSubjectPath(TriplesSameSubjectPathContext)">
                                            <node ID="ID_262" TEXT="varOrTerm(VarOrTermContext)">
                                                <node ID="ID_263" TEXT="var(VarContext)">
                                                    <node ID="ID_264" TEXT="?a"/>
                                                </node>
                                            </node>
                                            <node ID="ID_265" TEXT="propertyListPathNotEmpty(PropertyListPathNotEmptyContext)">
                                                <node ID="ID_266" TEXT="verbPath(VerbPathContext)">
                                                    <node ID="ID_267" TEXT="path(PathContext)">
                                                        <node ID="ID_268" TEXT="pathAlternative(PathAlternativeContext)">
                                                            <node ID="ID_269" TEXT="pathSequence(PathSequenceContext)">
                                                                <node ID="ID_270" TEXT="pathEltOrInverse(PathEltOrInverseContext)">
                                                                    <node ID="ID_271" TEXT="pathElt(PathEltContext)">
                                                                        <node ID="ID_272" TEXT="pathPrimary(PathPrimaryContext)">
                                                                            <node ID="ID_273" TEXT="iri(IriContext)">
                                                                                <node ID="ID_274" TEXT="prefixedName(PrefixedNameContext)">
                                                                                    <node ID="ID_275" TEXT=":適当"/>
                                                                                </node>
                                                                            </node>
                                                                        </node>
                                                                    </node>
                                                                </node>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                                <node ID="ID_276" TEXT="objectListPath(ObjectListPathContext)">
                                                    <node ID="ID_277" TEXT="objectPath(ObjectPathContext)">
                                                        <node ID="ID_278" TEXT="graphNodePath(GraphNodePathContext)">
                                                            <node ID="ID_279" TEXT="varOrTerm(VarOrTermContext)">
                                                                <node ID="ID_280" TEXT="var(VarContext)">
                                                                    <node ID="ID_281" TEXT="?url"/>
                                                                </node>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                        </node>
                                        <node ID="ID_282" TEXT="."/>
                                        <node ID="ID_283" TEXT="triplesSameSubjectPath(TriplesSameSubjectPathContext)">
                                            <node ID="ID_284" TEXT="varOrTerm(VarOrTermContext)">
                                                <node ID="ID_285" TEXT="var(VarContext)">
                                                    <node ID="ID_286" TEXT="?a"/>
                                                </node>
                                            </node>
                                            <node ID="ID_287" TEXT="propertyListPathNotEmpty(PropertyListPathNotEmptyContext)">
                                                <node ID="ID_288" TEXT="verbPath(VerbPathContext)">
                                                    <node ID="ID_289" TEXT="path(PathContext)">
                                                        <node ID="ID_290" TEXT="pathAlternative(PathAlternativeContext)">
                                                            <node ID="ID_291" TEXT="pathSequence(PathSequenceContext)">
                                                                <node ID="ID_292" TEXT="pathEltOrInverse(PathEltOrInverseContext)">
                                                                    <node ID="ID_293" TEXT="pathElt(PathEltContext)">
                                                                        <node ID="ID_294" TEXT="pathPrimary(PathPrimaryContext)">
                                                                            <node ID="ID_295" TEXT="iri(IriContext)">
                                                                                <node ID="ID_296" TEXT="prefixedName(PrefixedNameContext)">
                                                                                    <node ID="ID_297" TEXT=":種別"/>
                                                                                </node>
                                                                            </node>
                                                                        </node>
                                                                    </node>
                                                                </node>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                                <node ID="ID_298" TEXT="objectListPath(ObjectListPathContext)">
                                                    <node ID="ID_299" TEXT="objectPath(ObjectPathContext)">
                                                        <node ID="ID_300" TEXT="graphNodePath(GraphNodePathContext)">
                                                            <node ID="ID_301" TEXT="varOrTerm(VarOrTermContext)">
                                                                <node ID="ID_302" TEXT="var(VarContext)">
                                                                    <node ID="ID_303" TEXT="?x"/>
                                                                </node>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                        </node>
                                        <node ID="ID_304" TEXT="."/>
                                    </node>
                                </node>
                            </node>
                            <node ID="ID_305" TEXT="}"/>
                        </node>
                    </node>
                    <node ID="ID_306" TEXT="solutionModifier(SolutionModifierContext)"/>
                </node>
                <node ID="ID_307" TEXT="valuesClause(ValuesClauseContext)"/>
                <node ID="ID_308" TEXT="&lt;EOF&gt;"/>
            </node>
        </node>
    </node>
</map>
