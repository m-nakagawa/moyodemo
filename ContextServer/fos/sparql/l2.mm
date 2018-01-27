<?xml version="1.0" ?>
<map version="1.0.1">
    <!--FreeMindフォーマットです-->
    <node ID="ID_123" TEXT="../../Tests/Test8.sparql">
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
                <node ID="ID_135" TEXT="constructQuery(ConstructQueryContext)">
                    <node ID="ID_136" TEXT="CONSTRUCT"/>
                    <node ID="ID_137" TEXT="constructTemplate(ConstructTemplateContext)">
                        <node ID="ID_138" TEXT="{"/>
                        <node ID="ID_139" TEXT="constructTriples(ConstructTriplesContext)">
                            <node ID="ID_140" TEXT="triplesSameSubject(TriplesSameSubjectContext)">
                                <node ID="ID_141" TEXT="varOrTerm(VarOrTermContext)">
                                    <node ID="ID_142" TEXT="graphTerm(GraphTermContext)">
                                        <node ID="ID_143" TEXT="blankNode(BlankNodeContext)">
                                            <node ID="ID_144" TEXT="_:msg"/>
                                        </node>
                                    </node>
                                </node>
                                <node ID="ID_145" TEXT="propertyListNotEmpty(PropertyListNotEmptyContext)">
                                    <node ID="ID_146" TEXT="verb(VerbContext)">
                                        <node ID="ID_147" TEXT="varOrIRI(VarOrIRIContext)">
                                            <node ID="ID_148" TEXT="iri(IriContext)">
                                                <node ID="ID_149" TEXT="prefixedName(PrefixedNameContext)">
                                                    <node ID="ID_150" TEXT=":コマンド"/>
                                                </node>
                                            </node>
                                        </node>
                                    </node>
                                    <node ID="ID_151" TEXT="objectList(ObjectListContext)">
                                        <node ID="ID_152" TEXT="yobject(YobjectContext)">
                                            <node ID="ID_153" TEXT="graphNode(GraphNodeContext)">
                                                <node ID="ID_154" TEXT="varOrTerm(VarOrTermContext)">
                                                    <node ID="ID_155" TEXT="graphTerm(GraphTermContext)">
                                                        <node ID="ID_156" TEXT="iri(IriContext)">
                                                            <node ID="ID_157" TEXT="prefixedName(PrefixedNameContext)">
                                                                <node ID="ID_158" TEXT="ha:テキストメッセージ"/>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                        </node>
                                    </node>
                                </node>
                            </node>
                            <node ID="ID_159" TEXT="."/>
                            <node ID="ID_160" TEXT="constructTriples(ConstructTriplesContext)">
                                <node ID="ID_161" TEXT="triplesSameSubject(TriplesSameSubjectContext)">
                                    <node ID="ID_162" TEXT="varOrTerm(VarOrTermContext)">
                                        <node ID="ID_163" TEXT="graphTerm(GraphTermContext)">
                                            <node ID="ID_164" TEXT="blankNode(BlankNodeContext)">
                                                <node ID="ID_165" TEXT="_:msg"/>
                                            </node>
                                        </node>
                                    </node>
                                    <node ID="ID_166" TEXT="propertyListNotEmpty(PropertyListNotEmptyContext)">
                                        <node ID="ID_167" TEXT="verb(VerbContext)">
                                            <node ID="ID_168" TEXT="varOrIRI(VarOrIRIContext)">
                                                <node ID="ID_169" TEXT="iri(IriContext)">
                                                    <node ID="ID_170" TEXT="prefixedName(PrefixedNameContext)">
                                                        <node ID="ID_171" TEXT=":宛先"/>
                                                    </node>
                                                </node>
                                            </node>
                                        </node>
                                        <node ID="ID_172" TEXT="objectList(ObjectListContext)">
                                            <node ID="ID_173" TEXT="yobject(YobjectContext)">
                                                <node ID="ID_174" TEXT="graphNode(GraphNodeContext)">
                                                    <node ID="ID_175" TEXT="varOrTerm(VarOrTermContext)">
                                                        <node ID="ID_176" TEXT="var(VarContext)">
                                                            <node ID="ID_177" TEXT="?url"/>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                        </node>
                                    </node>
                                </node>
                                <node ID="ID_178" TEXT="."/>
                                <node ID="ID_179" TEXT="constructTriples(ConstructTriplesContext)">
                                    <node ID="ID_180" TEXT="triplesSameSubject(TriplesSameSubjectContext)">
                                        <node ID="ID_181" TEXT="varOrTerm(VarOrTermContext)">
                                            <node ID="ID_182" TEXT="graphTerm(GraphTermContext)">
                                                <node ID="ID_183" TEXT="blankNode(BlankNodeContext)">
                                                    <node ID="ID_184" TEXT="_:msg"/>
                                                </node>
                                            </node>
                                        </node>
                                        <node ID="ID_185" TEXT="propertyListNotEmpty(PropertyListNotEmptyContext)">
                                            <node ID="ID_186" TEXT="verb(VerbContext)">
                                                <node ID="ID_187" TEXT="varOrIRI(VarOrIRIContext)">
                                                    <node ID="ID_188" TEXT="iri(IriContext)">
                                                        <node ID="ID_189" TEXT="prefixedName(PrefixedNameContext)">
                                                            <node ID="ID_190" TEXT=":パラメータ"/>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                            <node ID="ID_191" TEXT="objectList(ObjectListContext)">
                                                <node ID="ID_192" TEXT="yobject(YobjectContext)">
                                                    <node ID="ID_193" TEXT="graphNode(GraphNodeContext)">
                                                        <node ID="ID_194" TEXT="varOrTerm(VarOrTermContext)">
                                                            <node ID="ID_195" TEXT="graphTerm(GraphTermContext)">
                                                                <node ID="ID_196" TEXT="rdfLiteral(RdfLiteralContext)">
                                                                    <node ID="ID_197" TEXT="string(StringContext)">
                                                                        <node ID="ID_198" TEXT="&quot;大変です&quot;"/>
                                                                    </node>
                                                                </node>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                        </node>
                                    </node>
                                    <node ID="ID_199" TEXT="."/>
                                </node>
                            </node>
                        </node>
                        <node ID="ID_200" TEXT="}"/>
                    </node>
                    <node ID="ID_201" TEXT="whereClause(WhereClauseContext)">
                        <node ID="ID_202" TEXT="WHERE"/>
                        <node ID="ID_203" TEXT="groupGraphPattern(GroupGraphPatternContext)">
                            <node ID="ID_204" TEXT="{"/>
                            <node ID="ID_205" TEXT="groupGraphPatternSub(GroupGraphPatternSubContext)">
                                <node ID="ID_206" TEXT="triplesBlock(TriplesBlockContext)">
                                    <node ID="ID_207" TEXT="triplesSameSubjectPath(TriplesSameSubjectPathContext)">
                                        <node ID="ID_208" TEXT="varOrTerm(VarOrTermContext)">
                                            <node ID="ID_209" TEXT="var(VarContext)">
                                                <node ID="ID_210" TEXT="?room"/>
                                            </node>
                                        </node>
                                        <node ID="ID_211" TEXT="propertyListPathNotEmpty(PropertyListPathNotEmptyContext)">
                                            <node ID="ID_212" TEXT="verbPath(VerbPathContext)">
                                                <node ID="ID_213" TEXT="path(PathContext)">
                                                    <node ID="ID_214" TEXT="pathAlternative(PathAlternativeContext)">
                                                        <node ID="ID_215" TEXT="pathSequence(PathSequenceContext)">
                                                            <node ID="ID_216" TEXT="pathEltOrInverse(PathEltOrInverseContext)">
                                                                <node ID="ID_217" TEXT="pathElt(PathEltContext)">
                                                                    <node ID="ID_218" TEXT="pathPrimary(PathPrimaryContext)">
                                                                        <node ID="ID_219" TEXT="iri(IriContext)">
                                                                            <node ID="ID_220" TEXT="prefixedName(PrefixedNameContext)">
                                                                                <node ID="ID_221" TEXT=":場所"/>
                                                                            </node>
                                                                        </node>
                                                                    </node>
                                                                </node>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                            <node ID="ID_222" TEXT="objectListPath(ObjectListPathContext)">
                                                <node ID="ID_223" TEXT="objectPath(ObjectPathContext)">
                                                    <node ID="ID_224" TEXT="graphNodePath(GraphNodePathContext)">
                                                        <node ID="ID_225" TEXT="varOrTerm(VarOrTermContext)">
                                                            <node ID="ID_226" TEXT="graphTerm(GraphTermContext)">
                                                                <node ID="ID_227" TEXT="iri(IriContext)">
                                                                    <node ID="ID_228" TEXT="prefixedName(PrefixedNameContext)">
                                                                        <node ID="ID_229" TEXT=":ここ"/>
                                                                    </node>
                                                                </node>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                        </node>
                                    </node>
                                    <node ID="ID_230" TEXT="."/>
                                    <node ID="ID_231" TEXT="triplesSameSubjectPath(TriplesSameSubjectPathContext)">
                                        <node ID="ID_232" TEXT="varOrTerm(VarOrTermContext)">
                                            <node ID="ID_233" TEXT="var(VarContext)">
                                                <node ID="ID_234" TEXT="?room"/>
                                            </node>
                                        </node>
                                        <node ID="ID_235" TEXT="propertyListPathNotEmpty(PropertyListPathNotEmptyContext)">
                                            <node ID="ID_236" TEXT="verbPath(VerbPathContext)">
                                                <node ID="ID_237" TEXT="path(PathContext)">
                                                    <node ID="ID_238" TEXT="pathAlternative(PathAlternativeContext)">
                                                        <node ID="ID_239" TEXT="pathSequence(PathSequenceContext)">
                                                            <node ID="ID_240" TEXT="pathEltOrInverse(PathEltOrInverseContext)">
                                                                <node ID="ID_241" TEXT="pathElt(PathEltContext)">
                                                                    <node ID="ID_242" TEXT="pathPrimary(PathPrimaryContext)">
                                                                        <node ID="ID_243" TEXT="iri(IriContext)">
                                                                            <node ID="ID_244" TEXT="prefixedName(PrefixedNameContext)">
                                                                                <node ID="ID_245" TEXT=":在室"/>
                                                                            </node>
                                                                        </node>
                                                                    </node>
                                                                </node>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                            <node ID="ID_246" TEXT="objectListPath(ObjectListPathContext)">
                                                <node ID="ID_247" TEXT="objectPath(ObjectPathContext)">
                                                    <node ID="ID_248" TEXT="graphNodePath(GraphNodePathContext)">
                                                        <node ID="ID_249" TEXT="varOrTerm(VarOrTermContext)">
                                                            <node ID="ID_250" TEXT="var(VarContext)">
                                                                <node ID="ID_251" TEXT="?p"/>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                        </node>
                                    </node>
                                    <node ID="ID_252" TEXT="."/>
                                    <node ID="ID_253" TEXT="triplesSameSubjectPath(TriplesSameSubjectPathContext)">
                                        <node ID="ID_254" TEXT="varOrTerm(VarOrTermContext)">
                                            <node ID="ID_255" TEXT="var(VarContext)">
                                                <node ID="ID_256" TEXT="?c"/>
                                            </node>
                                        </node>
                                        <node ID="ID_257" TEXT="propertyListPathNotEmpty(PropertyListPathNotEmptyContext)">
                                            <node ID="ID_258" TEXT="verbPath(VerbPathContext)">
                                                <node ID="ID_259" TEXT="path(PathContext)">
                                                    <node ID="ID_260" TEXT="pathAlternative(PathAlternativeContext)">
                                                        <node ID="ID_261" TEXT="pathSequence(PathSequenceContext)">
                                                            <node ID="ID_262" TEXT="pathEltOrInverse(PathEltOrInverseContext)">
                                                                <node ID="ID_263" TEXT="pathElt(PathEltContext)">
                                                                    <node ID="ID_264" TEXT="pathPrimary(PathPrimaryContext)">
                                                                        <node ID="ID_265" TEXT="iri(IriContext)">
                                                                            <node ID="ID_266" TEXT="prefixedName(PrefixedNameContext)">
                                                                                <node ID="ID_267" TEXT=":主人"/>
                                                                            </node>
                                                                        </node>
                                                                    </node>
                                                                </node>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                            <node ID="ID_268" TEXT="objectListPath(ObjectListPathContext)">
                                                <node ID="ID_269" TEXT="objectPath(ObjectPathContext)">
                                                    <node ID="ID_270" TEXT="graphNodePath(GraphNodePathContext)">
                                                        <node ID="ID_271" TEXT="varOrTerm(VarOrTermContext)">
                                                            <node ID="ID_272" TEXT="var(VarContext)">
                                                                <node ID="ID_273" TEXT="?p"/>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                        </node>
                                    </node>
                                    <node ID="ID_274" TEXT="."/>
                                    <node ID="ID_275" TEXT="triplesSameSubjectPath(TriplesSameSubjectPathContext)">
                                        <node ID="ID_276" TEXT="varOrTerm(VarOrTermContext)">
                                            <node ID="ID_277" TEXT="var(VarContext)">
                                                <node ID="ID_278" TEXT="?c"/>
                                            </node>
                                        </node>
                                        <node ID="ID_279" TEXT="propertyListPathNotEmpty(PropertyListPathNotEmptyContext)">
                                            <node ID="ID_280" TEXT="verbPath(VerbPathContext)">
                                                <node ID="ID_281" TEXT="path(PathContext)">
                                                    <node ID="ID_282" TEXT="pathAlternative(PathAlternativeContext)">
                                                        <node ID="ID_283" TEXT="pathSequence(PathSequenceContext)">
                                                            <node ID="ID_284" TEXT="pathEltOrInverse(PathEltOrInverseContext)">
                                                                <node ID="ID_285" TEXT="pathElt(PathEltContext)">
                                                                    <node ID="ID_286" TEXT="pathPrimary(PathPrimaryContext)">
                                                                        <node ID="ID_287" TEXT="iri(IriContext)">
                                                                            <node ID="ID_288" TEXT="prefixedName(PrefixedNameContext)">
                                                                                <node ID="ID_289" TEXT="ha:テキストメッセージ"/>
                                                                            </node>
                                                                        </node>
                                                                    </node>
                                                                </node>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                            <node ID="ID_290" TEXT="objectListPath(ObjectListPathContext)">
                                                <node ID="ID_291" TEXT="objectPath(ObjectPathContext)">
                                                    <node ID="ID_292" TEXT="graphNodePath(GraphNodePathContext)">
                                                        <node ID="ID_293" TEXT="varOrTerm(VarOrTermContext)">
                                                            <node ID="ID_294" TEXT="var(VarContext)">
                                                                <node ID="ID_295" TEXT="?url"/>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                        </node>
                                    </node>
                                    <node ID="ID_296" TEXT="."/>
                                </node>
                            </node>
                            <node ID="ID_297" TEXT="}"/>
                        </node>
                    </node>
                    <node ID="ID_298" TEXT="solutionModifier(SolutionModifierContext)"/>
                </node>
                <node ID="ID_299" TEXT="valuesClause(ValuesClauseContext)"/>
                <node ID="ID_300" TEXT="&lt;EOF&gt;"/>
            </node>
        </node>
    </node>
</map>
