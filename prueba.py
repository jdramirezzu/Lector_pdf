# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:17:52 2021

@author: analista4operaciones
"""

import sqlalchemy
import pandas as pd

engine = sqlalchemy.create_engine("mysql://mysql:reportserver@34.74.68.92:3306/BIServer")
sql_prueba = pd.read_sql_query("select coalesce(personas.identification,'') cedula_codeudor,coalesce(personas.razonsocial,'') nombre_codeudor,garantias.* from vista_garantias_con_tipo garantias left join cu_customermaster personas on (personas.cu_customermaster_id = garantias.cu_customermaster_id)", engine)

#sql_informacion_codeudores = pd.read_sql_query("select coalesce(`grt_tipo_garantia`.`descripcion`,'') AS `garantias_tipo`,coalesce(`grt_garantia`.`descripcion`,'') AS `Descripcion`,coalesce(`c`.`identification`,'') AS `Participante_Identificacion`,coalesce(`c`.`razonsocial`,'') AS `Participante_Nombre`,coalesce(`grt_garantia`.`cu_customermaster_id`,0) AS `cu_customermaster_id`,coalesce(`prm`.`numero_operacion`,0) AS `Numero_Prestamo`,coalesce(`prm`.`numero_pagare`,0) AS `Numero_Pagare`,coalesce(`cbl`.`name`,'') AS `Agencia`,`usuario`.`name` AS `Usuario_Modificacion` from (((((((((((((`grt_garantia` left join `grt_tipo_garantia` on((`grt_garantia`.`grt_tipo_garantia_id` = `grt_tipo_garantia`.`grt_tipo_garantia_id`))) left join `vw_rs_garantias_parte01_relacion` `relacion` on((`grt_garantia`.`grt_garantia_id` = `relacion`.`garantia`))) left join `grt_vehiculo` on((`grt_vehiculo`.`grt_garantia_id` = `grt_garantia`.`grt_garantia_id`))) left join `grt_seguro` on((`grt_seguro`.`grt_garantia_id` = `grt_garantia`.`grt_garantia_id`))) left join `grt_hipotecaria` on((`grt_hipotecaria`.`grt_garantia_id` = `grt_garantia`.`grt_garantia_id`))) left join `vw_rs_garantias_parte02_compania_seguros` `aseguradora` on((`aseguradora`.`codigo` = `grt_garantia`.`grt_garantia_id`))) left join `vw_rs_garantias_parte03_tipo_poliza` `tipo` on((`tipo`.`codigo` = `grt_garantia`.`grt_garantia_id`))) left join `vw_rs_garantias_parte05_tipo_inmueble` `descripcion` on((`descripcion`.`codigo` = `grt_garantia`.`grt_garantia_id`))) left join `cpo_garantia` `gcupo` on((`grt_garantia`.`grt_garantia_id` = `gcupo`.`grt_garantia_id`))) left join `prm_prestamo` `prm` on((`prm`.`numero_cupo` = `gcupo`.`cpo_cupo_id`))) left join `c_bpartner_location` `cbl` on((`prm`.`punto_venta` = `cbl`.`c_bpartner_location_id`))) left join `ad_user` `usuario` on((`grt_garantia`.`updatedby` = `usuario`.`ad_user_id`))) left join `cu_customermaster` `c` on((`relacion`.`cliente` = `c`.`cu_customermaster_id`)))",engine)


