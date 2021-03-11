# -*- coding: utf-8 -*-

HTML_OF_BANK_ACCOUNT = """
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
