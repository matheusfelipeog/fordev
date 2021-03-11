# -*- coding: utf-8 -*-

HTML_OF_BANK_ACCOUNT_INFOS = """
<div class="output-group">
    <div class="output-subtitle">Conta Corrente</div>
    <div id="conta_corrente" onclick="fourdevs.selectText(this)" class="output-txt output-txt-active">1370571-2<span class="clipboard-copy"></span></div>
</div>
<div class="output-group block">
    <div class="output-subtitle">Agência</div>
    <div id="agencia" onclick="fourdevs.selectText(this)" class="output-txt output-txt-active">1255<span class="clipboard-copy"></span></div>
</div>
<div class="output-group">
    <div class="output-subtitle">Banco</div>
    <div id="banco" onclick="fourdevs.selectText(this)" class="output-txt output-txt-active">Bradesco<span class="clipboard-copy"></span></div>
</div>
<div class="output-group block">
    <div class="output-subtitle">Cidade</div>
    <div id="cidade" onclick="fourdevs.selectText(this)" class="output-txt output-txt-active">Caieiras<span class="clipboard-copy"></span></div>
</div>
<div class="output-group">
    <div class="output-subtitle">Estado</div>
    <div id="estado" onclick="fourdevs.selectText(this)" class="output-txt output-txt-active">SP<span class="clipboard-copy"></span></div>
</div>

<div class="copy-info">Clique para copiar</div>
"""


HTML_OF_VEHICLE_INFOS = """
<h2 class="subtitulo_gerador">DADOS PESSOAIS:</h2>
<div class="row small-collapse">
    <div class="small-3 columns medium-text-right"><strong>Marca:</strong></div>
    <div class="small-4 columns"><input type="text" title="Marca" id="marca" value="Rolls-Royce" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-5 columns"><img id="bt_copy_marca" src="imagens/copy_clipboard.png" data-clipboard-target="marca" class="botao_copiar" title="Copiar" alt="Copiar" /></div>
</div>

<div class="row small-collapse">
    <div class="small-3 columns medium-text-right"><strong>Modelo:</strong></div>
    <div class="small-6 columns"><input type="text" title="Modelo" id="modelo" value="Wraith 6.6 V12 Aut." onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-3 columns"><img id="bt_copy_modelo" src="imagens/copy_clipboard.png" data-clipboard-target="modelo" class="botao_copiar" title="Copiar" alt="Copiar" /></div>
</div>

<div class="row small-collapse">
    <div class="small-3 columns medium-text-right"><strong>Ano:</strong></div>
    <div class="small-2 columns"><input type="text" title="Ano do Veículo" id="ano" value="2014" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-7 columns"><img id="bt_copy_ano" src="imagens/copy_clipboard.png" data-clipboard-target="ano" class="botao_copiar" title="Copiar" alt="Copiar" /></div>
</div>

<div class="row small-collapse">
    <div class="small-3 columns medium-text-right"><strong>RENAVAM:</strong></div>
    <div class="small-3 columns"><input type="text" title="Renavam" id="renavam" value="41047812580" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-6 columns"><img id="bt_copy_renavam" src="imagens/copy_clipboard.png" data-clipboard-target="renavam" class="botao_copiar" title="Copiar" alt="Copiar" /></div>
</div>

<div class="row small-collapse">
    <div class="small-3 columns medium-text-right"><strong>Placa:</strong></div>
    <div class="small-2 columns"><input type="text" title="Placa do Veículo" id="placa_veiculo" value="HVE-9411" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-7 columns"><img id="bt_copy_placa" src="imagens/copy_clipboard.png" data-clipboard-target="placa_veiculo" class="botao_copiar" title="Copiar" alt="Copiar" /></div>        
</div>

<div class="row small-collapse">
    <div class="small-3 columns medium-text-right"><strong>Cor:</strong></div>
    <div class="small-2 columns"><input type="text" title="Cor" id="cor" value="Verde" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-7 columns"><img id="bt_copy_cor" src="imagens/copy_clipboard.png" data-clipboard-target="cor" class="botao_copiar" title="Copiar" alt="Copiar" /></div>
</div>
"""


HTML_OF_CREDIT_CARD_INFOS = """
<div class="output-group">
    <div class="output-subtitle">Número do Cartão</div>
    <div id="cartao_numero" onclick="fourdevs.selectText(this)" class="output-txt output-txt-active">5016 0926 0945 3715 <span class="clipboard-copy"></span></div>
</div>

<div class="output-group block">
    <div class="output-subtitle">Data de Validade</div>
    <div id="data_validade" onclick="fourdevs.selectText(this)" class="output-txt output-txt-active">11/02/2023<span class="clipboard-copy"></span></div>
</div>

<div class="output-group">
    <div class="output-subtitle">Código Segurança (CVV)</div>
    <div id="codigo_seguranca" onclick="fourdevs.selectText(this)" class="output-txt output-txt-active">812<span class="clipboard-copy"></span></div>
</div>

<div class="copy-info">Clique para copiar</div>
"""


HTML_OF_COMPANY_INFOS = """
 <div class="row small-collapse">
    <div class="medium-3 columns medium-text-right"><strong>Nome:</strong></div>
    <div class="small-10 medium-7 columns"><input type="text" title="Nome" id="nome" value="Isabela e Cristiane Casa Noturna Ltda" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-2 columns"><img id="bt_copy_nome" src="imagens/copy_clipboard.png" data-clipboard-target="nome" class="botao_copiar" title="Copiar" alt="Copiar" /></div>
</div>

<div class="row small-collapse">
    <div class="medium-3 columns medium-text-right"><strong>CNPJ:</strong></div>
    <div class="small-10 medium-3 columns"><input type="text" title="CNPJ" id="cnpj" value="45.641.633/0001-17" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-2 medium-6 columns"><img id="bt_copy_cnpj" src="imagens/copy_clipboard.png" data-clipboard-target="cnpj" class="botao_copiar" title="Copiar" alt="Copiar" /></div>
</div>

<div class="row small-collapse">
    <div class="medium-3 columns medium-text-right"><strong>Inscrição Estadual:</strong></div>
    <div class="small-10 medium-3 columns"><input type="text" title="Inscrição Estadual" id="ie" value="040.102.816.356" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-2 medium-6 columns"><img id="bt_copy_ie" src="imagens/copy_clipboard.png" data-clipboard-target="ie" class="botao_copiar" title="Copiar" alt="Copiar" /></div>
</div>

<div class="row small-collapse">
    <div class="medium-3 columns medium-text-right"><strong>Data de Abertura:</strong></div>
    <div class="small-10 medium-2 columns"><input type="text" title="Data de Abertura" id="data_abertura" value="11/11/2020" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-2 medium-7 columns"><img id="bt_copy_data_abertura" src="imagens/copy_clipboard.png" data-clipboard-target="data_abertura" class="botao_copiar" title="Copiar" alt="Copiar" /></div>
</div>

<div class="row small-collapse">
    <div class="medium-3 columns medium-text-right"><strong>Site:</strong>
    </div>
    <div class="small-10 medium-7 columns"><input type="text" title="Site" id="site" value="www.isabelaecristianecasanoturnaltda.com.br" onFocus="this.select()" class="margem_menor" /></div>   
    <div class="small-2 columns"><img id="bt_copy_site" src="imagens/copy_clipboard.png" data-clipboard-target="site" class="botao_copiar" title="Copiar" /></div>
</div>

<div class="row small-collapse">
    <div class="medium-3 columns medium-text-right"><strong>E-Mail:</strong>
    </div>
    <div class="small-10 medium-7 columns"><input type="text" title="E-Mail" id="email" value="estoque@isabelaecristianecasanoturnaltda.com.br" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-2 columns"><img id="bt_copy_email" src="imagens/copy_clipboard.png" data-clipboard-target="email" class="botao_copiar" title="Copiar" /></div>
</div>

<div class="row small-collapse">
    <div class="medium-3 columns medium-text-right"><strong>CEP:</strong></div>
    <div class="small-10 medium-2 columns"><input type="text" title="CEP" id="cep" value="08559-240" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-2 medium-7 columns"><img id="bt_copy_cep" src="imagens/copy_clipboard.png" data-clipboard-target="cep" class="botao_copiar" title="Copiar" alt="Copiar" /></div>
</div>

<div class="row small-collapse">
    <div class="medium-3 columns medium-text-right"><strong>Endereço:</strong></div>
    <div class="small-10 medium-7 columns"><input type="text" title="Endereço" id="endereco" value="Rua Carmem Miranda" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-2 medium-2 columns"><img id="bt_copy_endereco" src="imagens/copy_clipboard.png" data-clipboard-target="endereco" class="botao_copiar" title="Copiar" alt="Copiar" /></div> 
</div>

<div class="row small-collapse">
    <div class="medium-3 columns medium-text-right"><strong>Número:</strong></div>
    <div class="small-10 medium-2 columns"><input type="text" title="Número" id="numero" value="872" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-2 medium-7 columns"><img id="bt_copy_numero" src="imagens/copy_clipboard.png" data-clipboard-target="numero" class="botao_copiar" title="Copiar" alt="Copiar" /></div>     
</div>

<div class="row small-collapse">
    <div class="medium-3 columns medium-text-right"><strong>Bairro:</strong></div>
    <div class="small-10 medium-7 columns"><input type="text" title="Bairro" id="bairro" value="Vila Jau" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-2 medium-2 columns"><img id="bt_copy_bairro" src="imagens/copy_clipboard.png" data-clipboard-target="bairro" class="botao_copiar" title="Copiar" alt="Copiar" /></div>     
</div>

<div class="row small-collapse">
    <div class="medium-3 columns medium-text-right"><strong>Cidade:</strong></div>
    <div class="small-10 medium-7 columns"><input type="text" title="Cidade" id="cidade" value="Poá" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-2 medium-2 columns"><img id="bt_copy_cidade" src="imagens/copy_clipboard.png" data-clipboard-target="cidade" class="botao_copiar" title="Copiar" alt="Copiar" /></div>     
</div>

<div class="row small-collapse">
    <div class="medium-3 columns medium-text-right"><strong>Estado:</strong></div>
    <div class="small-10 medium-1 columns"><input type="text" title="Estado" id="estado" value="SP" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-2 medium-8 columns"><img id="bt_copy_estado" src="imagens/copy_clipboard.png" data-clipboard-target="estado" class="botao_copiar" title="Copiar" alt="Copiar" /></div>     
</div>

<div class="row small-collapse">
    <div class="medium-3 columns medium-text-right"><strong>Telefone:</strong>
    </div>
    <div class="small-10 medium-3 columns"><input type="text" title="Telefone Fixo" id="telefone_fixo" value="(11) 3597-5594" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-2 medium-6 columns"><img id="bt_copy_telefone" src="imagens/copy_clipboard.png" data-clipboard-target="telefone_fixo" class="botao_copiar" title="Copiar" /></div>
</div>

<div class="row small-collapse">
    <div class="medium-3 columns medium-text-right"><strong>Celular:</strong>
    </div>
    <div class="small-10 medium-3 columns"><input type="text" title="Celular" id="celular" value="(11) 98491-8081" onFocus="this.select()" class="margem_menor" /></div>
    <div class="small-2 medium-6 columns"><img id="bt_copy_celular" src="imagens/copy_clipboard.png" data-clipboard-target="celular" class="botao_copiar" title="Copiar" /></div>
</div>
"""


HTML_OF_CITY_NAME = """
<option value=""></option>
<option value="7373">Alto Alegre</option>
<option value="7374">Amajari</option>
<option value="7375">Boa Vista</option>
<option value="7376">Bonfim</option>
<option value="7377">Cantá</option>
<option value="7378">Caracaraí</option>
<option value="7379">Caroebe</option>
<option value="7380">Iracema</option>
<option value="7381">Mucajaí</option>
<option value="7382">Normandia</option>
<option value="7383">Pacaraima</option>
<option value="7384">Rorainópolis</option>
<option value="7385">São João da Baliza</option>
<option value="7386">São Luiz</option>
<option value="7387">Uiramutã</option>
"""
