<?xml version="1.0" ?>
<map version="1.0.1">
    <!--FreeMindフォーマットです-->
    <node ID="ID_123" TEXT="Test4.sparql">
        <node ID="ID_124" POSITION="right" TEXT="root">
            <node ID="ID_125" TEXT="query(QueryContext)">
                <node ID="ID_126" TEXT="prologue(PrologueContext)">
                    <node ID="ID_127" TEXT="prefixDecl(PrefixDeclContext)">
                        <node ID="ID_128" TEXT="PREFIX"/>
                        <node ID="ID_129" TEXT=":"/>
                        <node ID="ID_130" TEXT="&lt;http://bizar.aitc.jp/ns/spaceos/0.1/&gt;"/>
                    </node>
                    <node ID="ID_131" TEXT="prefixDecl(PrefixDeclContext)">
                        <node ID="ID_132" TEXT="PREFIX"/>
                        <node ID="ID_133" TEXT="ha:"/>
                        <node ID="ID_134" TEXT="&lt;http://bizar.aitc.jp/ns/spaceos/0.1/人間API&gt;"/>
                    </node>
                </node>
                <node ID="ID_135" TEXT="selectQuery(SelectQueryContext)">
                    <node ID="ID_136" TEXT="selectClause(SelectClauseContext)">
                        <node ID="ID_137" TEXT="SELECT"/>
                        <node ID="ID_138" TEXT="selectVariables(SelectVariablesContext)">
                            <node ID="ID_139" TEXT="var(VarContext)">
                                <node ID="ID_140" TEXT="?url"/>
                            </node>
                        </node>
                    </node>
                    <node ID="ID_141" TEXT="whereClause(WhereClauseContext)">
                        <node ID="ID_142" TEXT="WHERE"/>
                        <node ID="ID_143" TEXT="groupGraphPattern(GroupGraphPatternContext)">
                            <node ID="ID_144" TEXT="{"/>
                            <node ID="ID_145" TEXT="groupGraphPatternSub(GroupGraphPatternSubContext)">
                                <node ID="ID_146" TEXT="triplesBlock(TriplesBlockContext)">
                                    <node ID="ID_147" TEXT="triplesSameSubjectPath(TriplesSameSubjectPathContext)">
                                        <node ID="ID_148" TEXT="varOrTerm(VarOrTermContext)">
                                            <node ID="ID_149" TEXT="var(VarContext)">
                                                <node ID="ID_150" TEXT="?room"/>
                                            </node>
                                        </node>
                                        <node ID="ID_151" TEXT="propertyListPathNotEmpty(PropertyListPathNotEmptyContext)">
                                            <node ID="ID_152" TEXT="verbPath(VerbPathContext)">
                                                <node ID="ID_153" TEXT="path(PathContext)">
                                                    <node ID="ID_154" TEXT="pathAlternative(PathAlternativeContext)">
                                                        <node ID="ID_155" TEXT="pathSequence(PathSequenceContext)">
                                                            <node ID="ID_156" TEXT="pathEltOrInverse(PathEltOrInverseContext)">
                                                                <node ID="ID_157" TEXT="pathElt(PathEltContext)">
                                                                    <node ID="ID_158" TEXT="pathPrimary(PathPrimaryContext)">
                                                                        <node ID="ID_159" TEXT="iri(IriContext)">
                                                                            <node ID="ID_160" TEXT="prefixedName(PrefixedNameContext)">
                                                                                <node ID="ID_161" TEXT=":場所"/>
                                                                            </node>
                                                                        </node>
                                                                    </node>
                                                                </node>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                            <node ID="ID_162" TEXT="objectListPath(ObjectListPathContext)">
                                                <node ID="ID_163" TEXT="objectPath(ObjectPathContext)">
                                                    <node ID="ID_164" TEXT="graphNodePath(GraphNodePathContext)">
                                                        <node ID="ID_165" TEXT="varOrTerm(VarOrTermContext)">
                                                            <node ID="ID_166" TEXT="graphTerm(GraphTermContext)">
                                                                <node ID="ID_167" TEXT="iri(IriContext)">
                                                                    <node ID="ID_168" TEXT="prefixedName(PrefixedNameContext)">
                                                                        <node ID="ID_169" TEXT=":ここ"/>
                                                                    </node>
                                                                </node>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                        </node>
                                    </node>
                                    <node ID="ID_170" TEXT="."/>
                                    <node ID="ID_171" TEXT="triplesSameSubjectPath(TriplesSameSubjectPathContext)">
                                        <node ID="ID_172" TEXT="varOrTerm(VarOrTermContext)">
                                            <node ID="ID_173" TEXT="var(VarContext)">
                                                <node ID="ID_174" TEXT="?room"/>
                                            </node>
                                        </node>
                                        <node ID="ID_175" TEXT="propertyListPathNotEmpty(PropertyListPathNotEmptyContext)">
                                            <node ID="ID_176" TEXT="verbPath(VerbPathContext)">
                                                <node ID="ID_177" TEXT="path(PathContext)">
                                                    <node ID="ID_178" TEXT="pathAlternative(PathAlternativeContext)">
                                                        <node ID="ID_179" TEXT="pathSequence(PathSequenceContext)">
                                                            <node ID="ID_180" TEXT="pathEltOrInverse(PathEltOrInverseContext)">
                                                                <node ID="ID_181" TEXT="pathElt(PathEltContext)">
                                                                    <node ID="ID_182" TEXT="pathPrimary(PathPrimaryContext)">
                                                                        <node ID="ID_183" TEXT="iri(IriContext)">
                                                                            <node ID="ID_184" TEXT="prefixedName(PrefixedNameContext)">
                                                                                <node ID="ID_185" TEXT=":在室"/>
                                                                            </node>
                                                                        </node>
                                                                    </node>
                                                                </node>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                            <node ID="ID_186" TEXT="objectListPath(ObjectListPathContext)">
                                                <node ID="ID_187" TEXT="objectPath(ObjectPathContext)">
                                                    <node ID="ID_188" TEXT="graphNodePath(GraphNodePathContext)">
                                                        <node ID="ID_189" TEXT="varOrTerm(VarOrTermContext)">
                                                            <node ID="ID_190" TEXT="var(VarContext)">
                                                                <node ID="ID_191" TEXT="?p"/>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                        </node>
                                    </node>
                                    <node ID="ID_192" TEXT="."/>
                                    <node ID="ID_193" TEXT="triplesSameSubjectPath(TriplesSameSubjectPathContext)">
                                        <node ID="ID_194" TEXT="varOrTerm(VarOrTermContext)">
                                            <node ID="ID_195" TEXT="var(VarContext)">
                                                <node ID="ID_196" TEXT="?c"/>
                                            </node>
                                        </node>
                                        <node ID="ID_197" TEXT="propertyListPathNotEmpty(PropertyListPathNotEmptyContext)">
                                            <node ID="ID_198" TEXT="verbPath(VerbPathContext)">
                                                <node ID="ID_199" TEXT="path(PathContext)">
                                                    <node ID="ID_200" TEXT="pathAlternative(PathAlternativeContext)">
                                                        <node ID="ID_201" TEXT="pathSequence(PathSequenceContext)">
                                                            <node ID="ID_202" TEXT="pathEltOrInverse(PathEltOrInverseContext)">
                                                                <node ID="ID_203" TEXT="pathElt(PathEltContext)">
                                                                    <node ID="ID_204" TEXT="pathPrimary(PathPrimaryContext)">
                                                                        <node ID="ID_205" TEXT="iri(IriContext)">
                                                                            <node ID="ID_206" TEXT="prefixedName(PrefixedNameContext)">
                                                                                <node ID="ID_207" TEXT=":主人"/>
                                                                            </node>
                                                                        </node>
                                                                    </node>
                                                                </node>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                            <node ID="ID_208" TEXT="objectListPath(ObjectListPathContext)">
                                                <node ID="ID_209" TEXT="objectPath(ObjectPathContext)">
                                                    <node ID="ID_210" TEXT="graphNodePath(GraphNodePathContext)">
                                                        <node ID="ID_211" TEXT="varOrTerm(VarOrTermContext)">
                                                            <node ID="ID_212" TEXT="var(VarContext)">
                                                                <node ID="ID_213" TEXT="?p"/>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                        </node>
                                    </node>
                                    <node ID="ID_214" TEXT="."/>
                                    <node ID="ID_215" TEXT="triplesSameSubjectPath(TriplesSameSubjectPathContext)">
                                        <node ID="ID_216" TEXT="varOrTerm(VarOrTermContext)">
                                            <node ID="ID_217" TEXT="var(VarContext)">
                                                <node ID="ID_218" TEXT="?c"/>
                                            </node>
                                        </node>
                                        <node ID="ID_219" TEXT="propertyListPathNotEmpty(PropertyListPathNotEmptyContext)">
                                            <node ID="ID_220" TEXT="verbPath(VerbPathContext)">
                                                <node ID="ID_221" TEXT="path(PathContext)">
                                                    <node ID="ID_222" TEXT="pathAlternative(PathAlternativeContext)">
                                                        <node ID="ID_223" TEXT="pathSequence(PathSequenceContext)">
                                                            <node ID="ID_224" TEXT="pathEltOrInverse(PathEltOrInverseContext)">
                                                                <node ID="ID_225" TEXT="pathElt(PathEltContext)">
                                                                    <node ID="ID_226" TEXT="pathPrimary(PathPrimaryContext)">
                                                                        <node ID="ID_227" TEXT="iri(IriContext)">
                                                                            <node ID="ID_228" TEXT="prefixedName(PrefixedNameContext)">
                                                                                <node ID="ID_229" TEXT="ha:テキストメッセージ"/>
                                                                            </node>
                                                                        </node>
                                                                    </node>
                                                                </node>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                            <node ID="ID_230" TEXT="objectListPath(ObjectListPathContext)">
                                                <node ID="ID_231" TEXT="objectPath(ObjectPathContext)">
                                                    <node ID="ID_232" TEXT="graphNodePath(GraphNodePathContext)">
                                                        <node ID="ID_233" TEXT="varOrTerm(VarOrTermContext)">
                                                            <node ID="ID_234" TEXT="var(VarContext)">
                                                                <node ID="ID_235" TEXT="?url"/>
                                                            </node>
                                                        </node>
                                                    </node>
                                                </node>
                                            </node>
                                        </node>
                                    </node>
                                    <node ID="ID_236" TEXT="."/>
                                </node>
                            </node>
                            <node ID="ID_237" TEXT="}"/>
                        </node>
                    </node>
                    <node ID="ID_238" TEXT="solutionModifier(SolutionModifierContext)"/>
                </node>
                <node ID="ID_239" TEXT="valuesClause(ValuesClauseContext)"/>
                <node ID="ID_240" TEXT="&lt;EOF&gt;"/>
            </node>
        </node>
    </node>
</map>
